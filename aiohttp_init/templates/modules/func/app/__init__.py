#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2019/10/12 13:26:04
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''


async def start_background_tasks(app):
    pass


def _init_route(app: Application) -> NoReturn:
    app.add_routes(
        [
            web.get('/proxies', get_proxies),
            web.post('/turn/{status}', control_status),
            web.delete('/proxies/{proxy}', delete_proxy),
        ]
    )


def _init_startup_task(app: Application) -> NoReturn:
    app.on_startup.append(start_background_tasks)


def _init_attrs(
        app: Application,
        queue: Queue
) -> NoReturn:
    app["queue"] = queue
    app['redis_client'] = get_client("redis")


def init_app(
        queue: Queue
) -> Application:
    app = web.Application()
    _init_attrs(
        app=app,
        queue=queue
    )
    _init_route(app=app)
    _init_startup_task(app=app)
    return app
