# -*-coding:utf-8-*-
"""
@author: 我的饭
@file: utils.py
@time: 2024/5/28 1:22
"""
import json
import time
from contextlib import contextmanager


class timeit_class:

    def __init__(self):
        self.total_time = 0

    def __enter__(self):
        self.start_time = time.time()
        print('--Started at:', self.start_time)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finished_time = time.time()
        print('--Finished at:', self.finished_time)
        print('--Total time:', self.finished_time - self.start_time)


@contextmanager
def timeit_method():
    try:
        start_time = time.time()
        print('--Started at:', start_time)
        yield
    finally:
        finished_time = time.time()
        print('--Finished at:', finished_time)
        print('--Total time:', finished_time - start_time)


class Utils:
    @staticmethod
    def read_config(path):
        with open(path, 'r') as f:
            config = json.load(f)
            return config
