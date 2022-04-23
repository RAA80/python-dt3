#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from time import sleep
from pymodbus.client.sync import ModbusSerialClient

from delta.client import Client
from delta.device import DT340

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    transport = ModbusSerialClient(method="rtu",
                                   port="COM5",
                                   baudrate=38400,
                                   stopbits=2,
                                   parity='N',
                                   bytesize=8,
                                   timeout=0.1,
                                   retry_on_empty=True)
    dt = Client(transport=transport, device=DT340, unit=1)
    print (dt)

    # Названия параметров соответствуют названиям на индикаторе прибора,
    # кроме начинающихся с подчеркивания

    for name in sorted(DT340.keys()):
        value = dt.getParam(name)
        print ("{:4s} = {}".format(name, value))
        sleep(0.1)

        result = dt.setParam(name, value)
        print ("{:4s} = {}".format(name, result))
        sleep(0.1)
