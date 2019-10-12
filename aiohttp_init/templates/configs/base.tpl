#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   base.py
@Time    :   2019/10/12 11:52:55
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''
import sys
from inspect import (
    getmembers
)
from pathlib import Path

# Base Config
BASE_PATH = Path(__file__).absolute().parent.parent
# Log Config
LOG_PATH = BASE_PATH/"log"


def check_path():
    module = sys.modules[__name__]
    members = getmembers(module)
    for name, value in members:
        if name.endswith("PATH") and not value.exists():
            value.mkdir(mode=0o777, parents=False, exist_ok=True)


check_path()
