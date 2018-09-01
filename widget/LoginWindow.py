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
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.resize(480, 260)
        self.setWindowFlags(QtCore.Qt.X11BypassWindowManagerHint | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.vBoxLayout = QtGui.QVBoxLayout()
        self.font = QtGui.QFont()
        self.font.setPixelSize(14)   # 设置字号32,以像素为单位
        self.font.setFamily("SimSun")# 设置字体，宋体
        self.font.setFamily(u"微软雅黑")
        # self.font.setWeight(20)    # 设置字型,不加粗
        self.font.setBold(True)
        self.font.setItalic(False)   # 设置字型,不倾斜
        self.font.setUnderline(False)# 设置字型,无下划线

        self.mailLabel = QtGui.QLabel("UserEmail: ")
        self.mailLabel.setFont(self.font)
        self.vBoxLayout.addWidget(self.mailLabel)
        self.centralwidget.setLayout(self.vBoxLayout)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    loginWin = LoginWindow()
    loginWin.show()
    sys.exit(app.exec_())

