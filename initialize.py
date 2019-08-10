#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   initialize.py
@Time    :   2019/08/10 14:37:02
@Author  :   linhanqiu
@PythonVersion  :   3.7
'''

import os
from pprint import pprint as print
from pathlib import Path
from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader


@dataclass
class Initialize:
    def get_config(self, user_custom):
        config = {
            "project_name": user_custom.get("project_name", "normal"),
            "project_host": user_custom.get("project_host", "normal"),
            "project_port": user_custom.get("project_port", "normal"),
        }
        return config

    def create(self, **kwargs):
        project_dir = Path(__file__).absolute().parent/kwargs["project_name"]
        templates_path = Path(__file__).absolute().parent/"templates"
        env = Environment(loader=FileSystemLoader(str(templates_path)))
        tpl_list = [tpl.replace("templates/", "")
                    for tpl in self.get_all_tpl(path=templates_path)]
        config = self.get_config(user_custom={
            "project_name": kwargs["project_name"],
            "project_host": kwargs["project_host"],
            "project_port": kwargs["project_port"],
        })
        for tpl_file in tpl_list:
            tpl = env.get_template(tpl_file)
            output = tpl.render(config)
            tpl_path = project_dir/tpl_file.replace("tpl", "py")
            if not tpl_path.parent.exists():
                tpl_path.parent.mkdir(mode=0o777, parents=True)
            with open(tpl_path, 'w+') as file:
                file.write(output)

    def get_all_tpl(self, path, parent=None):
        if not path.is_dir():
            return [f"{parent}/{path.name}" if parent else path.name]
        tpl_list = []
        for sub_path in path.iterdir():
            tpl_list.extend(self.get_all_tpl(
                sub_path, f"{parent}/{path.name}" if parent else path.name))
        return tpl_list
