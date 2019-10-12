#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   initialize.py
@Time    :   2019/08/10 14:37:02
@Author  :   linhanqiu
@PythonVersion  :   3.7
'''

import os
from typing import (
    NoReturn,
    Union,
    List,
    Dict,
    Any
)
from pprint import pprint as print
from pathlib import (
    Path,
    PureWindowsPath,
    PurePosixPath
)
from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader
from ..logger import logger

PATH = Union[PurePosixPath, PureWindowsPath, None]


@dataclass
class Initialize:
    def create(self, **kwargs) -> NoReturn:
        try:
            logger.info(f"Init Project: {kwargs['project_name']} Begin.")
            project_dir = Path(kwargs['project_path'])/kwargs["project_name"]
            templates_path = Path(
                __file__).absolute().parent.parent/"templates"
            env = Environment(loader=FileSystemLoader(str(templates_path)))
            tpl_list = [tpl.replace("templates/", "")
                        for tpl in self.get_all_tpl(path=templates_path)]
            for tpl_file in tpl_list:
                if tpl_file.endswith("py") or tpl_file.endswith("tpl"):
                    tpl = env.get_template(tpl_file)
                    output = tpl.render(kwargs)
                    tpl_path = project_dir/tpl_file.replace("tpl", "py")
                    if not tpl_path.parent.exists():
                        tpl_path.parent.mkdir(mode=0o777, parents=True)
                    self.create_handler(create_path=tpl_path, kwargs=kwargs)
                    with open(tpl_path, 'w+') as file:
                        file.write(output)
        except Exception:
            logger.error(Exception)
        else:
            logger.success(f"Init Project: {kwargs['project_name']} Success.")

    def get_all_tpl(self, path: PATH, parent: PATH = None) -> List[str]:
        if not path.is_dir():
            return [f"{parent}/{path.name}" if parent else path.name]
        tpl_list = []
        for sub_path in path.iterdir():
            tpl_list.extend(self.get_all_tpl(
                sub_path, f"{parent}/{path.name}" if parent else path.name))
        return tpl_list

    def create_handler(self, create_path: str, kwargs: Dict[str, Any]) -> NoReturn:
        if isinstance(create_path, PureWindowsPath):
            create_type = str(create_path).split("\\")[-2]

        def configs() -> NoReturn:
            for env in kwargs["project_envs"]:
                (create_path.parent/f'{env.lower()}.py').touch(mode=0o666)
        create_handlers = {
            "configs": configs
        }
        if create_type in create_handlers:
            create_handlers[create_type]()
