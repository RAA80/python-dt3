#! /usr/bin/env python3

"""Данный файл содержит настройки приборов."""

from typing import TypedDict, Union


class DELTA_PARAMS(TypedDict):
    address: int
    type: str
    divider: int
    min: Union[int, float]
    max: Union[int, float]


DELTA_DEVICE = dict[str, DELTA_PARAMS]


# Таблица настроек температурного контроллера DT3
DT3: DELTA_DEVICE = {
    "A1MA": {"address": 0x1116, "type": "U16", "divider": 1,    "min": 0,     "max": 100},     # Adjust Upper Limit of Analog Linear Output 1
    "A1MI": {"address": 0x1117, "type": "U16", "divider": 1,    "min": 0,     "max": 100},     # Adjust Lower Limit of Analog Linear Output 1
    "A2MA": {"address": 0x1118, "type": "U16", "divider": 1,    "min": 0,     "max": 100},     # Adjust Upper Limit of Analog Linear Output 2
    "A2MI": {"address": 0x1119, "type": "U16", "divider": 1,    "min": 0,     "max": 100},     # Adjust Lower Limit of Analog Linear Output 2
    "AL1D": {"address": 0x110B, "type": "U16", "divider": 1,    "min": 0,     "max": 100},     # Alarm 1 output delay time
    "AL1H": {"address": 0x1024, "type": "I16", "divider": 10,   "min": -9999, "max": 9999},    # Alarm 1 upper-limit
    "AL1L": {"address": 0x1025, "type": "I16", "divider": 10,   "min": -9999, "max": 9999},    # Alarm 1 lower-limit
    "AL1O": {"address": 0x1108, "type": "U16", "divider": 1,    "min": 0,     "max": 15},      # Alarm 1 function
    "AL2D": {"address": 0x110C, "type": "U16", "divider": 1,    "min": 0,     "max": 100},     # Alarm 2 output delay time
    "AL2H": {"address": 0x1026, "type": "I16", "divider": 10,   "min": -9999, "max": 9999},    # Alarm 2 upper-limit
    "AL2L": {"address": 0x1027, "type": "I16", "divider": 10,   "min": -9999, "max": 9999},    # Alarm 2 lower-limit
    "AL2O": {"address": 0x1109, "type": "U16", "divider": 1,    "min": 0,     "max": 15},      # Alarm 2 function
    "AL3D": {"address": 0x110D, "type": "U16", "divider": 1,    "min": 0,     "max": 100},     # Alarm 3 output delay time
    "AL3H": {"address": 0x1028, "type": "I16", "divider": 10,   "min": -9999, "max": 9999},    # Alarm 3 upper-limit
    "AL3L": {"address": 0x1029, "type": "I16", "divider": 10,   "min": -9999, "max": 9999},    # Alarm 3 lower-limit
    "AL3O": {"address": 0x110A, "type": "U16", "divider": 1,    "min": 0,     "max": 15},      # Alarm 3 function
    "ALA1": {"address": 0x1020, "type": "U16", "divider": 1,    "min": 0,     "max": 19},      # Alarm 1 type
    "ALA2": {"address": 0x1021, "type": "U16", "divider": 1,    "min": 0,     "max": 19},      # Alarm 2 type
    "ALA3": {"address": 0x1022, "type": "U16", "divider": 1,    "min": 0,     "max": 19},      # Alarm 3 type
    "AT":   {"address": 0x103B, "type": "U16", "divider": 1,    "min": 0,     "max": 1},       # AT setting
    "COEF": {"address": 0x100E, "type": "U16", "divider": 100,  "min": 0.01,  "max": 99.99},   # The setting of COEF when Dual Loop output control are used
    "COSH": {"address": 0x1039, "type": "U16", "divider": 1,    "min": 0,     "max": 1},       # Communication write status
    "CT1":  {"address": 0x1182, "type": "I16", "divider": 10,   "min": -9999, "max": 9999},    # CT1 Read Value
    "CT2":  {"address": 0x1183, "type": "I16", "divider": 10,   "min": -9999, "max": 9999},    # CT2 Read Value
    "CTRL": {"address": 0x1005, "type": "U16", "divider": 1,    "min": 0,     "max": 3},       # Control method
    "CTRS": {"address": 0x1120, "type": "U16", "divider": 1,    "min": 0,     "max": 3},       # SV control mode
    "D":    {"address": 0x100B, "type": "U16", "divider": 1,    "min": 0,     "max": 9999},    # Td Derivative time
    "DEAD": {"address": 0x100F, "type": "I16", "divider": 10,   "min": -99.9, "max": 999.9},   # The setting of Dead Band when Dual Loop output control are used
    "EVT1": {"address": 0x111C, "type": "U16", "divider": 1,    "min": 0,     "max": 4},       # Event 1 Selection
    "EVT2": {"address": 0x111D, "type": "U16", "divider": 1,    "min": 0,     "max": 4},       # Event 2 Selection
    "EVT3": {"address": 0x111E, "type": "U16", "divider": 1,    "min": 0,     "max": 4},       # Event 3 Selection
    "EXE2": {"address": 0x1126, "type": "U16", "divider": 1,    "min": 0,     "max": 1},       # Reserve the Programmable Running Status when Power OFF
    "EXEC": {"address": 0x1123, "type": "U16", "divider": 1,    "min": 0,     "max": 1},       # Positive/Negative Selection for Remote
    "FZ-R": {"address": 0x1127, "type": "U16", "divider": 1,    "min": 1,     "max": 10},      # Fuzzy Gain
    "FZDB": {"address": 0x1128, "type": "U16", "divider": 10,   "min": 0,     "max": 999.9},   # Fuzzy Dead Band
    "I":    {"address": 0x100A, "type": "U16", "divider": 1,    "min": 0,     "max": 9999},    # Ti Integral time
    "INPT": {"address": 0x1004, "type": "U16", "divider": 1,    "min": 0,     "max": 19},      # Input temperature sensor type
    "IOF":  {"address": 0x100C, "type": "U16", "divider": 10,   "min": 0,     "max": 100},     # Integration default
    "LOC":  {"address": 0x102C, "type": "U16", "divider": 1,    "min": 0,     "max": 1},       # Lock status
    "O1-C": {"address": 0x1007, "type": "U16", "divider": 10,   "min": 1,     "max": 990},     # 1st group of Heating/Cooling control cycle
    "O1-H": {"address": 0x1007, "type": "U16", "divider": 10,   "min": 1,     "max": 990},     # 1st group of Heating/Cooling control cycle
    "O1-S": {"address": 0x1010, "type": "I16", "divider": 10,   "min": -99.9, "max": 999.9},   # Hysteresis setting value of the 1st output group
    "O1MA": {"address": 0x110E, "type": "U16", "divider": 10,   "min": 0,     "max": 100},     # Upper limit of control output 1
    "O1MI": {"address": 0x110F, "type": "U16", "divider": 10,   "min": 0,     "max": 100},     # Lower limit of control output 1
    "O2-C": {"address": 0x1008, "type": "U16", "divider": 10,   "min": 1,     "max": 990},     # 2st group of Heating/Cooling control cycle
    "O2-H": {"address": 0x1008, "type": "U16", "divider": 10,   "min": 1,     "max": 990},     # 2st group of Heating/Cooling control cycle
    "O2-S": {"address": 0x1011, "type": "I16", "divider": 10,   "min": -99.9, "max": 999.9},   # Hysteresis setting value of the 2nd output group
    "O2MA": {"address": 0x1110, "type": "U16", "divider": 10,   "min": 0,     "max": 100},     # Upper limit of control output 2
    "O2MI": {"address": 0x1111, "type": "U16", "divider": 10,   "min": 0,     "max": 100},     # Lower limit of control output 2
    "OUT1": {"address": 0x1012, "type": "U16", "divider": 10,   "min": 0,     "max": 100},     # Output 1 value
    "OUT2": {"address": 0x1013, "type": "U16", "divider": 10,   "min": 0,     "max": 100},     # Output 2 value
    "P":    {"address": 0x1009, "type": "U16", "divider": 10,   "min": 0.1,   "max": 999.9},   # PB Proportional band
    "PDOF": {"address": 0x100D, "type": "U16", "divider": 10,   "min": 0,     "max": 100},     # Proportional control offset error value, when Ti=0
    "PID":  {"address": 0x101C, "type": "U16", "divider": 1,    "min": 0,     "max": 5},       # PID parameter selection
    "PTRN": {"address": 0x1030, "type": "U16", "divider": 1,    "min": 0,     "max": 15},      # Start pattern number
    "PV":   {"address": 0x1000, "type": "I16", "divider": 10,   "min": -9999, "max": 9999},    # Present value
    "PV-F": {"address": 0x1102, "type": "U16", "divider": 1,    "min": 0,     "max": 50},      # Temperature filter factor
    "PV-R": {"address": 0x1101, "type": "U16", "divider": 100,  "min": 0.1,   "max": 10},      # Temperature filter range
    "PVGA": {"address": 0x1100, "type": "U16", "divider": 1000, "min": 0,     "max": 1000},    # Adjust Temperature Gain
    "PVOF": {"address": 0x1016, "type": "I16", "divider": 10,   "min": -99.9, "max": 99.9},    # Temperature regulation value
    "R-S":  {"address": 0x103C, "type": "U16", "divider": 1,    "min": 0,     "max": 3},       # Control RUN/STOP setting
    "RM-F": {"address": 0x1121, "type": "I16", "divider": 1,    "min": -999,  "max": 999},     # Adjust Remote Compensation
    "RM-G": {"address": 0x1122, "type": "I16", "divider": 1,    "min": -999,  "max": 999},     # Adjust Remote Gain
    "RMTP": {"address": 0x1105, "type": "U16", "divider": 1,    "min": 0,     "max": 4},       # Remote Input Type Selection
    "RTMA": {"address": 0x111A, "type": "U16", "divider": 1,    "min": 0,     "max": 1000},    # Adjust Retransmission Upper Limit
    "RTMI": {"address": 0x111B, "type": "U16", "divider": 1,    "min": 0,     "max": 1000},    # Adjust Retransmission Lower Limit
    "S-HC": {"address": 0x1006, "type": "U16", "divider": 1,    "min": 0,     "max": 5},       # Heating/cooling control
    "SLOP": {"address": 0x1114, "type": "U16", "divider": 10,   "min": 0,     "max": 1000},    # Programmable Slope Increase
    "SP":   {"address": 0x1017, "type": "U16", "divider": 1,    "min": 0,     "max": 3},       # Analog decimal setting
    "STEP": {"address": 0x101F, "type": "U16", "divider": 1,    "min": 0,     "max": 15},      # Start step number
    "SV":   {"address": 0x1001, "type": "I16", "divider": 10,   "min": -9999, "max": 9999},    # Setpoint value
    "SVN":  {"address": 0x101D, "type": "I16", "divider": 10,   "min": 0,     "max": 100},     # SV value corresponded to PID value
    "SVSL": {"address": 0x1104, "type": "U16", "divider": 10,   "min": 0,     "max": 10},      # Slope of Temperature Increase
    "TP-H": {"address": 0x1002, "type": "I16", "divider": 10,   "min": -9999, "max": 9999},    # Upper-limit of temperature range
    "TP-L": {"address": 0x1003, "type": "I16", "divider": 10,   "min": -9999, "max": 9999},    # Lower-limit of temperature range
    "TPUN": {"address": 0x103A, "type": "U16", "divider": 1,    "min": 0,     "max": 1},       # Temperature unit display selection
    "TUNE": {"address": 0x1106, "type": "U16", "divider": 1,    "min": 0,     "max": 1},       # AT Control
    "W-TM": {"address": 0x1113, "type": "U16", "divider": 1,    "min": 0,     "max": 900},     # Programmable Waiting Time
    "WTSV": {"address": 0x1112, "type": "U16", "divider": 1,    "min": 0,     "max": 1000},    # Programmable Waiting Temeprature

    "_BTN": {"address": 0x102B, "type": "U16", "divider": 1,    "min": 0,     "max": 255},     # Read Pushbutton Status
    "_CJC": {"address": 0x1125, "type": "U16", "divider": 1,    "min": 0,     "max": 1},       # Cold Junction Compensation
    "_IRS": {"address": 0x1107, "type": "U16", "divider": 1,    "min": 0,     "max": 1},       # Remote Input Reverse Setting
    "_LED": {"address": 0x102A, "type": "U16", "divider": 1,    "min": 0,     "max": 255},     # Read LED Status
    "_ORV": {"address": 0x1103, "type": "U16", "divider": 1,    "min": 0,     "max": 3},       # Reverse Output
    "_SAV": {"address": 0x1129, "type": "U16", "divider": 1,    "min": 0,     "max": 1},       # Save Programmable Settings into Memory
    "_SSL": {"address": 0x1124, "type": "U16", "divider": 1,    "min": 0,     "max": 1},       # Switch Slope Time Unit
    "_TST": {"address": 0x1115, "type": "U16", "divider": 1,    "min": 0,     "max": 0},       # Testing Mode
    "_VER": {"address": 0x102F, "type": "U16", "divider": 1,    "min": 0,     "max": 65535},   # Software version
}
