#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/13
Desc  : 登陆窗口
"""
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow, QWidget
from util.SkinHelper import SkinHelper


class LoginWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        SkinHelper().setStyle(self, ':/qss/titlebar_style.qss')
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.resize(480, 260)
        self.setWindowFlags(QtCore.Qt.X11BypassWindowManagerHint | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.vBoxLayout = QtGui.QVBoxLayout()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    loginWin = LoginWindow()
    loginWin.show()
    sys.exit(app.exec_())

