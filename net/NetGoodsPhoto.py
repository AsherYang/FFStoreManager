#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/5/6
Desc:   商品详情图片类，网络传递数据

"""


class NetGoodsPhoto:

    def __init__(self):
        self._photo = None
        self._thum_photo = None

    @property
    def photo(self):
        return self._photo

    @photo.setter
    def photo(self, value):
        self._photo = value

    @property
    def thum_photo(self):
        return self._thum_photo

    @thum_photo.setter
    def thum_photo(self, value):
        self._thum_photo = value
