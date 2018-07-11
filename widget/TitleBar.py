#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/11
Desc  : 自定义标题栏
https://blog.csdn.net/liang19890820/article/details/50555298
"""

from PyQt4.QtGui import QWidget, QLabel, QPushButton, QSizePolicy, QHBoxLayout, QIcon, QPalette
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from util.QtFontUtil import QtFontUtil


class TitleBar(QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setFixedHeight(30)

        self.mPIconLabel = QLabel()
        self.mPTitleLabel = QLabel()
        self.mPMinimizeBtn = QLabel()
        self.mPMaximizeBtn = QLabel()
        self.mPCloseBtn = QLabel()

        self.mPIconLabel.setFixedSize(20, 20)
        # !!必须要设置这一项，表示大小随内容缩放，配合等宽高setFixedSize，控件随图片按照等比缩放内容
        self.mPIconLabel.setScaledContents(True)
        self.mPTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.mPTitleLabel.setFont(QtFontUtil().getFont('Microsoft YaHei', 12))

        self.mPMinimizeBtn.setFixedSize(20, 20)
        self.mPMaximizeBtn.setFixedSize(20, 20)
        self.mPCloseBtn.setFixedSize(20, 20)

        self.mPTitleLabel.setObjectName(u'titleLabel')
        self.mPMinimizeBtn.setObjectName(u'minimizeBtn')
        self.mPMaximizeBtn.setObjectName(u'maximizeBtn')
        self.mPCloseBtn.setObjectName(u'closeBtn')

        self.mPMinimizeBtn.setPixmap(QtGui.QPixmap(':/darkqss/dark_img/close-hover.png'))
        self.mPMaximizeBtn.setPixmap(QtGui.QPixmap(':/darkqss/dark_img/close-pressed.png'))
        self.mPCloseBtn.setPixmap(QtGui.QPixmap(':/darkqss/dark_img/close.png'))
        # !!必须要设置这一项，表示大小随内容缩放，配合等宽高setFixedSize，控件随图片按照等比缩放内容
        self.mPMinimizeBtn.setScaledContents(True)
        self.mPMaximizeBtn.setScaledContents(True)
        self.mPCloseBtn.setScaledContents(True)

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
        self.setLayout(hBoxLayout)

    def setLogo(self, icon_path):
        self.mPIconLabel.setPixmap(QtGui.QPixmap(icon_path))

    def setTitle(self, title):
        self.mPTitleLabel.setText(title)
