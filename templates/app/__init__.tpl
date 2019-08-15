#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from typing import NoReturn
from aiohttp import web
from aiohttp.web import Application
from config import *
from logger import logger
from clients import get_client


def _init_attrs(app: Application) -> NoReturn:
    app["{{project_name}}"] = "{{project_name}}"
    app["redis"] = get_client(client_type="redis")
    app["mysql"] = get_client(client_type="mysql")


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
    for resource in app.router.resources():
        logger.info(f"Register Route:{resource.url_for()}")


def init_app() -> Application:
    app = Application()
    _init_route(app=app)
    _init_attrs(app=app)
    _init_startup_task(app=app)
    return app


async def run_app() -> NoReturn:
    logger.info("App init Begin.")
    app = init_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, APP_HOST, APP_PORT)
    logger.info(f"App init Success, Server listen at {APP_HOST}:{APP_PORT}")
    await site.start()
