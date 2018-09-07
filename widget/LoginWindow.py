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
        self.font.setPixelSize(14)  # 设置字号32,以像素为单位
        self.font.setFamily("SimSun")  # 设置字体，宋体
        self.font.setFamily(u"微软雅黑")
        # self.font.setWeight(20)    # 设置字型,不加粗
        self.font.setBold(True)
        self.font.setItalic(False)  # 设置字型,不倾斜
        self.font.setUnderline(False)  # 设置字型,无下划线

        self.palette = QtGui.QPalette()
        self.palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        # mail
        self.mailHBoxLayout = QtGui.QHBoxLayout()
        self.mailLabel = QtGui.QLabel("UserEmail: ")
        self.mailLabel.setFont(self.font)
        self.mailLabel.setPalette(self.palette)
        self.mailEditLabel = QtGui.QLineEdit()
        self.mailEditLabel.setFont(self.font)
        self.mailEditLabel.setPalette(self.palette)
        self.mailEditLabel.setTextMargins(10, 0, 10, 0)
        self.mailHBoxLayout.addStretch(1)
        self.mailHBoxLayout.addWidget(self.mailLabel)
        self.mailHBoxLayout.addWidget(self.mailEditLabel)
        self.mailHBoxLayout.addStretch(1)
        # password
        self.pwdHBoxLayout = QtGui.QHBoxLayout()
        self.pwdLabel = QtGui.QLabel("Password: ")
        self.pwdLabel.setFont(self.font)
        self.pwdLabel.setPalette(self.palette)
        self.pwdEditLabel = QtGui.QLineEdit()
        self.pwdEditLabel.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdEditLabel.setFont(self.font)
        self.pwdEditLabel.setPalette(self.palette)
        self.pwdEditLabel.setTextMargins(10, 0, 10, 0)
        self.pwdHBoxLayout.addStretch(1)
        self.pwdHBoxLayout.addWidget(self.pwdLabel)
        self.pwdHBoxLayout.addWidget(self.pwdEditLabel)
        self.pwdHBoxLayout.addStretch(1)
        # Login
        self.loginHBoxLayout = QtGui.QHBoxLayout()
        self.loginBtn = QtGui.QPushButton()
        self.loginBtn.setObjectName(u'loginBtn')
        self.loginBtn.setText(u'登陆')
        self.loginBtn.setFont(self.font)
        self.loginHBoxLayout.addWidget(self.loginBtn)

        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addLayout(self.mailHBoxLayout)
        self.vBoxLayout.addLayout(self.pwdHBoxLayout)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addLayout(self.loginHBoxLayout)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.setContentsMargins(40, 40, 40, 40)
        self.centralwidget.setLayout(self.vBoxLayout)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    loginWin = LoginWindow()
    loginWin.show()
    sys.exit(app.exec_())
