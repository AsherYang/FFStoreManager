#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/16
Desc  : 实现跨模块的全局变量

模块需求: 保存整个应用程序的全局变量
1. 在登陆后，保存登陆信息，以便于后面其他接口获取登陆信息。而不必重复查询数据库

https://www.cnblogs.com/suwings/p/6358061.html
"""


"""
初始化，只在main 中调用一次
"""
def init():
    global _global_dict
    _global_dict = {}

"""
定义一个全局变量
"""
def setValue(key, value):
    _global_dict[key] = value

"""
获取一个全局变量值，不存在，则返回默认值
"""
def getValue(key, defValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue
