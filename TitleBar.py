#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/11
Desc  : 自定义标题栏
https://blog.csdn.net/liang19890820/article/details/50555298
"""

from PyQt4.QtGui import QWidget, QLabel, QPushButton, QSizePolicy, QHBoxLayout
from PyQt4 import QtCore


class TitleBar(QWidget):
    def __init__(self, *args, **kwargs):
        self.setFixedHeight(30)
        self.mPIconLabel = QLabel()
        self.mPTitleLabel = QLabel()
        self.mPMinimizeBtn = QPushButton()
        self.mPMaximizeBtn = QPushButton()
        self.mPCloseBtn = QPushButton()

        self.mPIconLabel.setFixedSize(20, 20)
        self.mPIconLabel.setScaledContents(True)

        self.mPTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.mPMinimizeBtn.setFixedSize(27, 22)
        self.mPMaximizeBtn.setFixedSize(27, 22)
        self.mPCloseBtn.setFixedSize(27, 22)

        self.mPTitleLabel.setObjectName(u'titleLabel')
        self.mPMinimizeBtn.setObjectName(u'minimizeBtn')
        self.mPMaximizeBtn.setObjectName(u'maximizeBtn')
        self.mPCloseBtn.setObjectName(u'closeBtn')

        self.mPMinimizeBtn.setToolTip('Minimize')
        self.mPMaximizeBtn.setToolTip('Maximize')
        self.mPCloseBtn.setToolTip('close')

        hBoxLayout = QHBoxLayout()
        hBoxLayout.addWidget(self.mPIconLabel)
        hBoxLayout.addSpacing(5)
        hBoxLayout.addWidget(self.mPTitleLabel)
        hBoxLayout.addWidget(self.mPMinimizeBtn)
        hBoxLayout.addWidget(self.mPMaximizeBtn)
        hBoxLayout.addWidget(self.mPCloseBtn)
        hBoxLayout.addSpacing(0)
        hBoxLayout.setContentsMargins(5, 0, 5, 0)
        self.setLayout(hBoxLayout)
        self.connect(self.mPMinimizeBtn, QtCore.SIGNAL('clicked(bool)'), self.onClick)
        self.connect(self.mPMaximizeBtn, QtCore.SIGNAL('clicked(bool)'), self.onClick)
        self.connect(self.mPCloseBtn, QtCore.SIGNAL('clicked(bool)'), self.onClick)

    # 双击标题栏进行界面的最大化和还原操作
    def mouseDoubleClickEvent(self, QMouseEvent):
        self.mPMaximizeBtn.emit(QtCore.SIGNAL('clicked()'))

    # 支持鼠标进行界面拖动
    def mousePressEvent(self, QMouseEvent):
        pass

    # 设置界面标题和图标
    def eventFilter(self, QObject, QEvent):
        pass

    # 进行最大化和还原
    def updateMaximize(self):
        pass

    # 进行最小化，最大化/还原，关闭操作
    def onClick(self):
        pass

    def isInTitleBar(self, xPos, yPos):
        return yPos < 30

