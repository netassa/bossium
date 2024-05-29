# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: utils.py
@time: 2024/5/28 1:22
"""
import json


class Utils:
    @staticmethod
    def read_config(path):
        with open(path, 'r') as f:
            config = json.load(f)
            return config
