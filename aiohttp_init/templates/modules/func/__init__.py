#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2019/10/12 13:23:58
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''


def entry():
    app = init_app(queue=queue)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(
        runner=runner,
        host=PROXY_HOST,
        port=PROXY_PORT
    )
    await site.start()
