#! /usr/bin/env python3

"""Пример использования библиотеки."""

from delta.client import Client
from pymodbus.client.sync import ModbusSerialClient

if __name__ == "__main__":
    transport = ModbusSerialClient(method="rtu",    # default 19200-8-N-1
                                   port="COM5",
                                   timeout=0.1,
                                   retry_on_empty=True)
    client = Client(transport=transport, unit=1)
    print(client)

    name = "SV"       # Остальные названия параметров в файле 'device.py'
    value = client.get_param(name)
    print(f"{name} = {value}")

    result = client.set_param(name, value)
    print(f"{name} = {result}")
