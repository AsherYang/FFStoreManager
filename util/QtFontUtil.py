#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/11
Desc  : 字体设置工具类
"""
from PyQt4.QtGui import QFont
from PyQt4 import QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class QtFontUtil:
    def __init__(self):
        pass

    def getFont(self, font_family, font_size=10):
        font = QFont()
        font.setFamily(_fromUtf8(font_family))
        font.setPointSize(font_size)
        font.setFixedPitch(True)
        return font