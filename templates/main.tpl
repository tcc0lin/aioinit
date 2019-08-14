#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import asyncio
from aiohttp import web
from app import run_app
from clients import init_all_clients

_loop = asyncio.get_event_loop()
_loop.run_until_complete(init_all_clients())
asyncio.ensure_future(run_app())
_loop.run_forever()