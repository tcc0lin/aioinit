#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
from typing import NoReturn
from inspect import (
    getmembers,
    isfunction
)
import aioredis
from config import *
from logger import logger
_clients = {}


async def _init_redis() -> NoReturn:
    redis_client = await aioredis.create_redis_pool(
        address=f'redis://{REDIS_HOST}:{REDIS_PORT}',
        encoding="utf-8"
    )
    _clients["redis"] = redis_client


async def _init_mysql() -> NoReturn:
    pass


async def init_all_clients() -> NoReturn:
    module = sys.modules[__name__]
    members = getmembers(module, predicate=isfunction)
    for func_name, func in members:
        if func_name.startswith("_"):
            logger.info(f"Clients-{func_name} init Begin")
            await func()
            logger.info(f"Clients-{func_name} init Success")


def get_client(client_type: str):
    return _clients.get(client_type, None)
