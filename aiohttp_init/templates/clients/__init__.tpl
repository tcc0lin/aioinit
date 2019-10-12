#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2019/10/12 13:20:27
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''

import sys
from typing import NoReturn
from inspect import (
    getmembers,
    isfunction
)
import aioredis
from configs import *
from logger import config_logger
_clients = {}


async def _init_redis() -> NoReturn:
    redis_client = await aioredis.create_redis_pool(
        address=f'redis://{REDIS_HOST}:{REDIS_PORT}',
        password=REDIS_PASSWORD,
        encoding="utf-8",
        maxsize=REDIS_MAXSIZE
    )
    _clients["redis"] = redis_client


async def init_all_clients() -> NoReturn:
    logger = config_logger(module_name="clients")
    module = sys.modules[__name__]
    members = getmembers(module, predicate=isfunction)
    for func_name, func in members:
        if func_name.startswith("_"):
            logger.info(f"{func_name} Begin")
            try:
                await func()
            except Exception as e:
                logger.error(f"{func_name} Fail")
            else:
                logger.info(f"{func_name} Success")


def get_client(client_type: str):
    return _clients.get(client_type, None)
