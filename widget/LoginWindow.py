#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/13
Desc  : 登陆窗口
"""
from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow, QWidget


class LoginWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

