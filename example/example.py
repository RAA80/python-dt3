#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from pymodbus.client.sync import ModbusSerialClient

from delta.client import Client
from delta.device import DT340

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    transport = ModbusSerialClient(method="rtu",    # default 19200-8-N-1
                                   port="COM5",
                                   timeout=0.1,
                                   retry_on_empty=True)
    dt = Client(transport=transport, device=DT340, unit=1)
    print(dt)

    name = "SV"     # Остальные названия параметров в файле 'device.py'
    value = dt.get_param(name)
    print("{:4s} = {}".format(name, value))

    result = dt.set_param(name, value)
    print("{:4s} = {}".format(name, result))
