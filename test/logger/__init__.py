#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
from loguru import logger
from configs import *
config = {
    "handlers": [
        {
            "sink": f"{LOG_PATH}/test.log",
            "enqueue": True,
            "retention": "10 days"
        },
        {
            "sink": sys.stdout,
            "enqueue": True,
        },
    ],
    "extra": {"project": 'test'}
}
logger.configure(**config)