#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/18
Desc  : 商品goods 尺码颜色类，网络传递数据
"""


class NetGoodsSizeColor:
    def __init__(self):
        self._attr_size = None
        self._attr_color = None

    @property
    def attr_size(self):
        return self._attr_size

    @attr_size.setter
    def attr_size(self, value):
        self._attr_size = value

    @property
    def attr_color(self):
        return self._attr_color

    @attr_color.setter
    def attr_color(self, value):
        self._attr_color = value
