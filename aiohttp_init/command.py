#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   command.py
@Time    :   2019/10/11 15:09:47
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''

import argparse
from typing import NoReturn
from pathlib import Path
from .core.initialize import Initialize
from .logger import logger

parser = argparse.ArgumentParser(
    description='Auto Create Robust Web Projects Of Python3 For Humans'
)
parser.add_argument(
    "-N",
    "--name",
    default="test",
    help='Customize Project Name'
)
parser.add_argument(
    "-P",
    "--path",
    default=str(Path(__file__).absolute().parent.parent),
    help='Customize Project Storage Path'
)
args = parser.parse_args()


def main() -> NoReturn:
    init = Initialize()
    init.create(
        project_name=args.name,
        project_path=args.path,
    )
