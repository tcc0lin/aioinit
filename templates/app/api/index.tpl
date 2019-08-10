#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from aiohttp import web
from aiohttp.web import (
    Response,
    Request
)


async def index(request) -> Response:
    return web.json_response(
        data={"{{project_name}}": "ok"}
    )
