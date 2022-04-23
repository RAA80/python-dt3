#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
from pymodbus.constants import Endian
from pymodbus.version import version
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
        return ("Client(transport={}, unit={})".format(self._socket, self.unit))

    def _errorCheck(self, name, retcode):
        if not retcode:         # for python2 and pymodbus v1.3.0
            _logger.error("Unit {} called '{}' with error: "
                          "Modbus Error: [Input/Output] No Response received "
                          "from the remote unit".format(self.unit, name))
        elif isinstance(retcode, (ModbusException, ExceptionResponse)):
            _logger.error("Unit {} called '{}' with error: {}".
                            format(self.unit, name, retcode))
        else:
            return True

    def getParam(self, name):
        ''' Чтение значения параметра по заданному имени '''

        name = name.upper()
        self._dev = self.device[name]

        result = self._socket.read_holding_registers(address=self._dev['address'],
                                                     count=1,
                                                     unit=self.unit)
        if self._errorCheck(name, result):
            if int(version.short()[0]) > 1:
                decoder = BinaryPayloadDecoder.fromRegisters(registers=result.registers,
                                                             byteorder=Endian.Big,
                                                             wordorder=Endian.Big)
            else:
                decoder = BinaryPayloadDecoder.fromRegisters(registers=result.registers,
                                                             endian=Endian.Big)
            if self._dev['type'] == "U16":
                return decoder.decode_16bit_uint() if self._dev['divider'] == 1 \
                       else decoder.decode_16bit_uint()/self._dev['divider']
            elif self._dev['type'] == "I16":
                return decoder.decode_16bit_int() if self._dev['divider'] == 1 \
                       else decoder.decode_16bit_int()/self._dev['divider']

    def setParam(self, name, value):
        ''' Запись значения параметра по заданному имени '''

        name = name.upper()
        self._dev = self.device[name]

        if value < self._dev['min'] or value > self._dev['max']:
            raise ValueError("Parameter '{}' out of range ({}, {})".
                             format(name, self._dev['min'], self._dev['max']))

        if int(version.short()[0]) > 1:
            builder = BinaryPayloadBuilder(byteorder=Endian.Big,
                                           wordorder=Endian.Big)
        else:
            builder = BinaryPayloadBuilder(endian=Endian.Big)

        value *= self._dev['divider']
        if self._dev['type'] == "U16":   builder.add_16bit_uint(int(value))
        elif self._dev['type'] == "I16": builder.add_16bit_int(int(value))

        payload = builder.build()

        result = self._socket.write_registers(address=self._dev['address'],
                                              values=payload,
                                              skip_encode=True,
                                              unit=self.unit)
        return self._errorCheck(name, result)


__all__ = [ "Client" ]
