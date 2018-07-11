#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/7/12
Desc:   系统托盘类

https://www.cnblogs.com/jikeboy/p/6526274.html
http://doc.qt.io/qt-5/qsystemtrayicon.html
"""
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QSystemTrayIcon, QIcon, QMenu


class TrayIcon(QSystemTrayIcon):
    def __init__(self):
        QtGui.QSystemTrayIcon.__init__(self)
        # 设置关闭所有窗口,也不关闭应用程序
        QtGui.QApplication.instance().setQuitOnLastWindowClosed(False)
        # 设置系统托盘图标
        self.setIcon(QIcon(":/whiteqss/white_img/nscc.png"))
        # 托盘被点击
        self.activated.connect(self.trayClickActive)
        # 托盘消息被点击
        self.messageClicked.connect(self.showMsg)
        self.menu = QMenu()
        self.quitAction = QtGui.QAction("退出", self, triggered=self.quit)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

    def trayClickActive(self, reason):
        # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        # http://doc.qt.io/qt-5/qsystemtrayicon.html  (ActivationReason)
        if reason == QSystemTrayIcon.DoubleClick or reason == QSystemTrayIcon.Trigger:
            pw = self.parent()
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()
        elif reason == QSystemTrayIcon.Context:
            self.showMenu()
        print reason

    def showMsg(self, msg):
        # self.showMessage("提示", "你点了消息", self.icon)
        # http://doc.qt.io/qt-5/qsystemtrayicon.html (MessageIcon)
        self.show()
        self.showMessage("FFStore", msg, icon=2)

    def showMenu(self):
        self.menu.show()

    def quit(self):
        self.setVisible(False)
        self.parent().exit()
        QtGui.QApplication.quit()
        sys.exit()
