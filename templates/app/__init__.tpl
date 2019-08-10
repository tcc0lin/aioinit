#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from typing import NoReturn
from aiohttp import web
from aiohttp.web import Application


def _init_attrs(app: Application) -> NoReturn:
    app["{{project_name}}"] = "{{project_name}}"


def _init_startup_task(app: Application) -> NoReturn:
    async def start_background_tasks(app):
        pass
    app.on_startup.append(start_background_tasks)


def _init_route(app: Application) -> NoReturn:
    from .api.index import index
    app.add_routes(
        [
            web.get('/index', index),
            web.post('/index', index),
            web.delete('/index', index),
        ]
    )


def init_app() -> Application:
    app = Application()
    _init_route(app=app)
    _init_attrs(app=app)
    _init_startup_task(app=app)
    return app
