#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2019/10/12 10:51:36
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''


import os
import sys
import importlib
from .base import *
ALLOWED_DEPLOY_TYPE = ['DEV', 'PROD', 'TEST']
DEPLOY_TYPE = os.environ.get('TEST', 'DEV')
if DEPLOY_TYPE not in ALLOWED_DEPLOY_TYPE:
    raise Exception('Deployment type {} is not allowed'.format(DEPLOY_TYPE))
sub_config_name = DEPLOY_TYPE.lower()
configs = importlib.import_module(f'.{sub_config_name}', __name__)
self_module = sys.modules[__name__]
for attr_name in dir(configs):
    if attr_name[0].isupper():
        setattr(self_module, attr_name, getattr(configs, attr_name))