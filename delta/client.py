#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
from pymodbus.constants import Endian
from pymodbus.exceptions import ModbusException
from pymodbus.pdu import ExceptionResponse

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


class Client(object):
    ''' Класс управления температурным контроллером серии DT3 '''

    def __init__(self, transport, device, unit):
        self._socket = transport
        if not self._socket.connect():
            raise Exception("Socket not connected")

        self.device = device
        self.unit = unit

    def __del__(self):
        if self._socket:
            self._socket.close()

    def __repr__(self):
        return "Client(transport={}, unit={})".format(self._socket, self.unit)

    def _error_check(self, retcode):
        if isinstance(retcode, (ModbusException, ExceptionResponse, type(None))):
            _logger.error("Unit %d return %s", self.unit, retcode)
        else:
            return True

    def get_param(self, name):
        ''' Чтение значения параметра по заданному имени '''

        name = name.upper()
        dev = self.device[name]

        result = self._socket.read_holding_registers(address=dev['address'],
                                                     count=1,
                                                     unit=self.unit)
        if self._error_check(result):
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big)

            if dev['type'] == "U16":
                return decoder.decode_16bit_uint() if dev['divider'] == 1 \
                       else decoder.decode_16bit_uint()/dev['divider']
            elif dev['type'] == "I16":
                return decoder.decode_16bit_int() if dev['divider'] == 1 \
                       else decoder.decode_16bit_int()/dev['divider']

    def set_param(self, name, value):
        ''' Запись значения параметра по заданному имени '''

        name = name.upper()
        dev = self.device[name]

        if value is None or value < dev['min'] or value > dev['max']:
            raise ValueError("Parameter '{}' out of range ({}, {}) value '{}'".
                             format(name, dev['min'], dev['max'], value))

        builder = BinaryPayloadBuilder(None, Endian.Big)

        value *= dev['divider']
        {"U16": lambda value: builder.add_16bit_uint(int(value)),
         "I16": lambda value: builder.add_16bit_int(int(value))
        }[dev['type']](value)

        result = self._socket.write_registers(address=dev['address'],
                                              values=builder.build(),
                                              skip_encode=True,
                                              unit=self.unit)
        return self._error_check(result)


__all__ = [ "Client" ]
