#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   setup.py
@Time    :   2019/10/11 15:44:26
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''

from setuptools import setup
from setuptools import find_packages
setup(
    name="aiohttp_init",          # 包名
    version="0.0.1",              # 版本信息
    packages=find_packages(),  # 要打包的项目文件夹
    include_package_data=True,    # 自动打包文件夹内所有数据
    zip_safe=True,                # 设定项目包为安全，不用每次都检测其安全性

    install_requires=[          # 安装依赖的其他包
        "certifi==2019.9.11",
        "colorama==0.4.1",
        "Jinja2==2.10.3",
        "loguru==0.3.2",
    ],
    python_requires='>=3',
    # 设置程序的入口为hello
    # 安装后，命令行执行hello相当于调用hello.py中的main方法
    entry_points={
        'console_scripts': [
            'aiohttp_init = aiohttp_init.command:main'
        ]
    },

    # 如果要上传到PyPI，则添加以下信息
    author="lateautumn4lin",
    author_email="linhanqiu1123@163.com",
    description="Aiohttp officially recommends automatic generation libraries",
    license="MIT",
    keywords="Aiohttp Officially",
)
