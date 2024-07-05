#! /usr/bin/env python3

"""Реализация класса клиента для управления температурным контроллером
Delta серии DT3.
"""

from pymodbus.client.sync import ModbusSerialClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.pdu import ModbusResponse


class DeltaError(Exception):
    pass


class Client:
    """Класс управления температурным контроллером Delta серии DT3."""

    def __init__(self, transport: ModbusSerialClient, device: dict, unit: int) -> None:
        """Инициализация класса клиента с указанными параметрами."""

        self.socket = transport
        self.socket.connect()

        self.device = device
        self.unit = unit

    def __del__(self) -> None:
        """Закрытие соединения с устройством при удалении объекта."""

        if self.socket:
            self.socket.close()

    def __repr__(self) -> str:
        """Строковое представление объекта."""

        return f"{type(self).__name__}(socket={self.socket}, unit={self.unit})"

    @staticmethod
    def _check_error(retcode: ModbusResponse) -> bool:
        """Проверка возвращаемого значения на ошибку."""

        if retcode.isError():
            raise DeltaError(retcode)
        return True

    def _check_name(self, name: str) -> dict:
        """Проверка названия параметра."""

        name = name.upper()
        if name not in self.device:
            msg = f"Unknown parameter '{name}'"
            raise DeltaError(msg)

        return self.device[name]

    def get_param(self, name: str) -> float:
        """Чтение данных из устройства."""

        dev = self._check_name(name)

        result = self.socket.read_holding_registers(address=dev["address"],
                                                    unit=self.unit)
        self._check_error(result)

        decoder = BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big)
        value = {"U16": decoder.decode_16bit_uint,
                 "I16": decoder.decode_16bit_int,
                }[dev["type"]]()
        return value if dev["divider"] == 1 else value / dev["divider"]

    def set_param(self, name: str, value: float) -> bool:
        """Запись данных в устройство."""

        dev = self._check_name(name)

        if value is None or value < dev["min"] or value > dev["max"]:
            msg = f"An '{name}' value of '{value}' is out of range"
            raise DeltaError(msg)

        builder = BinaryPayloadBuilder(None, Endian.Big)

        value *= dev["divider"]
        {"U16": builder.add_16bit_uint,
         "I16": builder.add_16bit_int,
        }[dev["type"]](int(value))

        result = self.socket.write_registers(address=dev["address"],
                                             values=builder.build(),
                                             skip_encode=True,
                                             unit=self.unit)
        return self._check_error(result)


__all__ = ["Client"]
