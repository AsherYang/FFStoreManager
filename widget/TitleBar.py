#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/11
Desc  : 自定义标题栏
https://blog.csdn.net/liang19890820/article/details/50555298
https://blog.csdn.net/qq_38528972/article/details/78573591
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QLabel, QPushButton, QSizePolicy, QHBoxLayout, QApplication

from util.QtFontUtil import QtFontUtil
from util.SkinHelper import SkinHelper


# 将父类从QWidget 改为QMainWindow，可控制边框距离等
class TitleBar(QMainWindow):
    def __init__(self, parent):
        QtGui.QMainWindow.__init__(self, parent)
        SkinHelper().setStyle(self, ':/qss/titlebar_style.qss')
        self.setFixedHeight(30)

        self.mPIconLabel = QLabel()
        self.mPTitleLabel = QLabel()
        self.mPMinimizeBtn = QPushButton()
        self.mPMaximizeBtn = QPushButton()
        self.mPCloseBtn = QPushButton()

        self.mPIconLabel.setFixedSize(20, 20)
        # !!必须要设置这一项，表示大小随内容缩放，配合等宽高setFixedSize，控件随图片按照等比缩放内容
        self.mPIconLabel.setScaledContents(True)
        self.mPTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.mPTitleLabel.setFont(QtFontUtil().getFont(u'微软雅黑', 14, True))

        self.mPMinimizeBtn.setFixedSize(20, 20)
        self.mPMaximizeBtn.setFixedSize(20, 20)
        self.mPCloseBtn.setFixedSize(20, 20)

        self.mPTitleLabel.setObjectName(u'titleLabel')
        self.mPMinimizeBtn.setObjectName(u'minimizeBtn')
        self.mPMaximizeBtn.setObjectName(u'maximizeBtn')
        self.mPCloseBtn.setObjectName(u'closeBtn')

        # self.mPMinimizeBtn.setPixmap(QtGui.QPixmap(':/darkqss/dark_img/close-hover.png'))
        # self.mPMaximizeBtn.setPixmap(QtGui.QPixmap(':/darkqss/dark_img/close-pressed.png'))
        # self.mPCloseBtn.setPixmap(QtGui.QPixmap(':/darkqss/dark_img/close.png'))
        # !!必须要设置这一项，表示大小随内容缩放，配合等宽高setFixedSize，控件随图片按照等比缩放内容
        # self.mPMinimizeBtn.setScaledContents(True)
        # self.mPMaximizeBtn.setScaledContents(True)
        # self.mPCloseBtn.setScaledContents(True)

        hBoxLayout = QHBoxLayout()
        hBoxLayout.addWidget(self.mPIconLabel)
        hBoxLayout.addSpacing(5)
        hBoxLayout.addWidget(self.mPTitleLabel)
        hBoxLayout.addWidget(self.mPMinimizeBtn)
        hBoxLayout.addWidget(self.mPMaximizeBtn)
        hBoxLayout.addWidget(self.mPCloseBtn)
        # 控件之间的间距
        hBoxLayout.addSpacing(0)
        # 控件与窗体之间的间距
        hBoxLayout.setContentsMargins(5, 0, 5, 0)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # 这里使用的信号槽方式有3种，以后可以参考下，理一下思路。这里都是实验ok的。
        self.connect(self.mPMinimizeBtn, QtCore.SIGNAL('clicked()'), self.parent(), QtCore.SLOT('showMinimized()'))
        self.connect(self.mPMaximizeBtn, QtCore.SIGNAL('clicked()'), self.maximizeBtnClick)
        self.connect(self.mPCloseBtn, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
        self.widget = QtGui.QWidget()
        self.widget.setMouseTracking(True)
        self.widget.setLayout(hBoxLayout)
        self.setCentralWidget(self.widget)

    def setLogo(self, icon_path):
        self.mPIconLabel.setPixmap(QtGui.QPixmap(icon_path))

    def setTitle(self, title):
        self.mPTitleLabel.setText(title)

    def minimizeBtnClick(self):
        self.emit(QtCore.SIGNAL('minimizeProSignal'))

    def maximizeBtnClick(self):
        self.emit(QtCore.SIGNAL('maximaxProSignal'))

    def minimizeProSignal(self):
        return

    def maximaxProSignal(self):
        return


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    TitleBar = TitleBar()
    TitleBar.show()
    sys.exit(app.exec_())