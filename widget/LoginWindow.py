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
from util.QtFontUtil import QtFontUtil

from util.SkinHelper import SkinHelper
from net.LoginHttp import LoginHttp
from util.ThreadUtil import ThreadUtil


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
        self.palette = QtGui.QPalette()
        self.palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.red)
        # mail
        self.mailHBoxLayout = QtGui.QHBoxLayout()
        self.mailLabel = QtGui.QLabel("UserEmail:")
        self.mailLabel.setFixedWidth(82)
        self.mailLabel.setFont(QtFontUtil().getFont('微软雅黑', 14, True))
        self.mailLabel.setPalette(self.palette)
        self.mailEditLabel = QtGui.QLineEdit()
        self.mailEditLabel.setObjectName(u'loginEdit')
        self.mailEditLabel.setFont(QtFontUtil().getFont('微软雅黑', 14, True))
        self.mailEditLabel.setPalette(self.palette)
        self.mailEditLabel.setTextMargins(10, 0, 10, 0)
        self.mailHBoxLayout.addStretch(1)
        self.mailHBoxLayout.addWidget(self.mailLabel)
        self.mailHBoxLayout.addWidget(self.mailEditLabel)
        self.mailHBoxLayout.addStretch(1)
        # password
        self.pwdHBoxLayout = QtGui.QHBoxLayout()
        self.pwdLabel = QtGui.QLabel("Password:")
        self.pwdLabel.setFixedWidth(80)
        self.pwdLabel.setFont(QtFontUtil().getFont('微软雅黑', 14, True))
        self.pwdLabel.setPalette(self.palette)
        self.pwdEditLabel = QtGui.QLineEdit()
        self.pwdEditLabel.setObjectName(u'loginEdit')
        self.pwdEditLabel.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdEditLabel.setFont(QtFontUtil().getFont('微软雅黑', 14, True))
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
        self.loginBtn.setFont(QtFontUtil().getFont('微软雅黑', 14, True))
        self.loginBtn.connect(self.loginBtn, QtCore.SIGNAL('clicked()'), self.loginByThread)
        self.loginHBoxLayout.addWidget(self.loginBtn)

        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addLayout(self.mailHBoxLayout)
        self.vBoxLayout.addLayout(self.pwdHBoxLayout)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.addLayout(self.loginHBoxLayout)
        self.vBoxLayout.addStretch(1)
        self.vBoxLayout.setContentsMargins(40, 40, 40, 40)
        self.centralwidget.setLayout(self.vBoxLayout)

    def login(self, userEmail, userPwd):
        print 'useEmail: %s , usePwd: %s' % (userEmail, userPwd)
        if not userEmail or not userPwd:
            self.loginBtn.setText(u'请输入用户名和密码')
            return False
        loginHttp = LoginHttp()
        self.loginBtn.setText(u'登陆中')
        loginResult = loginHttp.login(user_tel=userEmail, sms_pwd=userPwd)
        print 'loginResult: ', loginResult
        if loginResult:
            self.loginBtn.setText(u'登陆成功')
        else:
            self.loginBtn.setText(u'登陆失败')
        self.emit(QtCore.SIGNAL('loginStatusSignal(bool)'), loginResult)
        return loginResult

    def loginByThread(self):
        userEmail = str(self.mailEditLabel.text())
        userPwd = str(self.pwdEditLabel.text())
        threadUtil = ThreadUtil(funcName=self.login, userEmail=userEmail, userPwd=userPwd)
        threadUtil.setDaemon(True)
        threadUtil.start()

    def loginStatusSignal(self, loginStatus):
        return


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    loginWin = LoginWindow()
    loginWin.show()
    sys.exit(app.exec_())
