#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aiohttp import web
from app import init_app

app = init_app()
web.run_app(app)
