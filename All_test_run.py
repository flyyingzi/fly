#coding=utf-8
import unittest
from pyselenium import TestRunner


if __name__ == '__main__':

    runner = TestRunner('./', '百度测试用例', '测试环境：Firefox')
    runner.run()