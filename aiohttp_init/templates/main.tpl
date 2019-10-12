#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/10/12 12:21:45
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''

import asyncio
import argparse
import importlib
from logger import logger
from clients import (
    init_all_clients
)

_loop = asyncio.get_event_loop()
_loop.run_until_complete(init_all_clients())
parser = argparse.ArgumentParser(description='{{project_name}}')
parser.add_argument('--module', default="", help='Choose A Operational Module')
args = parser.parse_args()
modules = importlib.import_module(f"modules.{args.module}")
getattr(modules, "entry")()
_loop.run_forever()
