#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   command.py
@Time    :   2019/08/10 14:49:29
@Author  :   linhanqiu
@PythonVersion  :   3.7
'''
import argparse
from initialize import Initialize
from logger import logger

parser = argparse.ArgumentParser(description='auto create new aiohttp project')
parser.add_argument('--name', default="normal", help='choose a project_name')
parser.add_argument('--host', default="127.0.0.1", help='choose a host')
parser.add_argument('--port', default=8000, help='choose a port')
args = parser.parse_args()


def init():
    try:
        init = Initialize()
        init.create(
            project_name=args.name,
            project_host=args.host,
            project_port=args.port
        )
    except Exception as e:
        logger.info(e)


init()
