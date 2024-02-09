#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from pymodbus.constants import Endian
from pymodbus.exceptions import ModbusException
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.pdu import ExceptionResponse

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


class Client(object):
    """ Класс управления температурным контроллером серии DT3. """

    def __init__(self, transport, device, unit):
        self._socket = transport
        if not self._socket.connect():
            msg = "Socket not connected"
            raise Exception(msg)

        self.device = device
        self.unit = unit

    def __del__(self):
        if self._socket:
            self._socket.close()

    def __repr__(self):
        return "Client(transport={}, unit={})".format(self._socket, self.unit)

    def _error_check(self, retcode):
        if not isinstance(retcode, (ModbusException, ExceptionResponse, type(None))):
            return True
        _logger.error("Unit %d return %s", self.unit, retcode)

    def get_param(self, name):
        """ Чтение значения параметра по заданному имени. """

        name = name.upper()
        dev = self.device[name]

        result = self._socket.read_holding_registers(address=dev["address"],
                                                     count=1,
                                                     unit=self.unit)
        if self._error_check(result):
            decoder = BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big)

            return {"U16": {True: lambda: decoder.decode_16bit_uint(),
                            False: lambda: decoder.decode_16bit_uint() / dev["divider"]},
                    "I16": {True: lambda: decoder.decode_16bit_int(),
                            False: lambda: decoder.decode_16bit_int() / dev["divider"]},
                   }[dev["type"]][dev["divider"] == 1]()

    def set_param(self, name, value):
        """ Запись значения параметра по заданному имени. """

        name = name.upper()
        dev = self.device[name]

        if value is None or value < dev["min"] or value > dev["max"]:
            msg = "An '{}' value of '{}' is out of range".format(name, value)
            raise ValueError(msg)

        builder = BinaryPayloadBuilder(None, Endian.Big)

        value *= dev["divider"]
        {"U16": lambda value: builder.add_16bit_uint(int(value)),
         "I16": lambda value: builder.add_16bit_int(int(value)),
        }[dev["type"]](value)

        result = self._socket.write_registers(address=dev["address"],
                                              values=builder.build(),
                                              skip_encode=True,
                                              unit=self.unit)
        return self._error_check(result)


__all__ = ["Client"]
