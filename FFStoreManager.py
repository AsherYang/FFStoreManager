#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
UI_Author: zhang
Email:  ouyangfan1991@gmail.com
Date:   2018/7/8
Desc:   后台首页   

界面参考:  https://github.com/harry159821/XiamiForLinuxProject
https://github.com/HuberTRoy/MusicBox
"""

import StringIO
import os
import sys
sys.path.append('../')

import threading
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtNetwork import QLocalServer, QLocalSocket
from PyQt4.QtGui import QSizePolicy, QCursor, QDesktopWidget, QLabel, QPushButton
from constant import AppConstants
from util.QtFontUtil import QtFontUtil
from qss import style_rc
from util.SkinHelper import SkinHelper
from widget.TitleBar import TitleBar
from widget.TrayIcon import TrayIcon
from widget.LoginWindow import LoginWindow
from constant import GlobalVar

reload(sys)
# print sys.getdefaultencoding()
sys.setdefaultencoding('utf8')
# print sys.getdefaultencoding()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Ui_MainWidget(object):
    def setupUi(self, mainWindow, localServer, argv=None):
        self.mainwindow = mainWindow
        # 解决多终端问题 http://www.oschina.net/code/snippet_54100_629
        self.localServer = localServer

        # 获取当前脚本所在的目录
        # self.sysArg0 = argv[0]

        mainWindow.setObjectName(_fromUtf8("MainWindow"))
        # MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.statusBar = QtGui.QStatusBar(mainWindow)
        self.menubar = QtGui.QMenuBar()
        menubarFont = self.menubar.font()
        menubarFont.setPointSize(12)
        # menubarFont.setFamily("宋体")
        # menubarFont.setFamily("Monospace")
        menubarFont.setFamily("Microsoft YaHei")
        self.menubar.setFont(menubarFont)

        adminLogin = self.menubar.addMenu(u' &登录')
        managerUser = self.menubar.addMenu(u'&用户管理')
        managerCate = self.menubar.addMenu(u'&分类管理')
        managerGoods = self.menubar.addMenu(u'&商品管理')
        managerOrder = self.menubar.addMenu(u'&订单管理')
        managerBanner = self.menubar.addMenu(u'&公告管理')
        managerOther = self.menubar.addMenu(u' &其他')
        # 设置固定大小，注意添加菜单后，需要增加对应的width，此处是为了能够控制窗口大小，以便鼠标拖动
        self.menubar.setFixedWidth(550)

        # =============== action ======================
        # managerUser action
        userQueryAction = QtGui.QAction(u'用户查询', mainWindow)
        userQueryAction.setStatusTip(_fromUtf8('可根据手机号查询用户'))
        # managerOther action
        otherExpressAction = QtGui.QAction(u'快递查询', mainWindow)
        otherExpressAction.setIcon(QtGui.QIcon(":/dardqss/dark_img/branch_open-on.png"))
        otherExpressAction.setStatusTip(_fromUtf8('可根据快递单号或者订单号查询'))
        # otherExpressAction.connect(otherExpressAction, QtCore.SIGNAL('triggered()'), self.)
        otherBillAction = QtGui.QAction(u'账单统计', mainWindow)
        otherBillAction.setStatusTip(_fromUtf8('账单查询'))
        # =============== action ======================

        # =============== 控件 ======================
        self.ShowMsgEdit = QtGui.QTextEdit()
        self.ShowMsgEdit.setFont(QtFontUtil().getFont('Monospace', 10))
        self.ShowMsgEdit.setText(u'showMsgEdit')
        self.cateTreeWidget = QtGui.QTreeWidget()
        self.goodsListWidget = QtGui.QListWidget()
        # =============== 控件 ======================

        managerUser.addAction(userQueryAction)
        managerOther.addAction(otherExpressAction)
        managerOther.addAction(otherBillAction)

        # 添加到 mainWindow
        # mainWindow.setMenuBar(self.menubar)
        mainWindow.setStatusBar(self.statusBar)

        # vBoxLayout 和 hBoxLayout 的选择依据是：根据2个控件的排列方向，上下排(vBoxLayout)还是左右排(hBoxLayout)
        vBoxLayout = QtGui.QVBoxLayout()
        hBboxLayout = QtGui.QHBoxLayout()

        hCateGoodsBoxLayout = QtGui.QHBoxLayout()
        # 控件之间的间距
        hCateGoodsBoxLayout.setSpacing(10)
        # 控件与窗体之间的间距
        hCateGoodsBoxLayout.setContentsMargins(10, 10, 10, 0)

        # 获取大小策略
        cateTreeSizePolicy = self.cateTreeWidget.sizePolicy()
        goodsListSizePolicy = self.goodsListWidget.sizePolicy()
        # 缩放策略
        cateTreeSizePolicy.setHorizontalPolicy(QSizePolicy.Maximum)
        goodsListSizePolicy.setHorizontalPolicy(QSizePolicy.Expanding)
        # 缩放因子
        cateTreeSizePolicy.setHorizontalStretch(1)
        goodsListSizePolicy.setHorizontalStretch(2)
        self.cateTreeWidget.setSizePolicy(cateTreeSizePolicy)
        self.goodsListWidget.setSizePolicy(goodsListSizePolicy)

        hCateGoodsBoxLayout.addWidget(self.cateTreeWidget)
        hCateGoodsBoxLayout.addWidget(self.goodsListWidget)
        hBboxLayout.addLayout(hCateGoodsBoxLayout)
        # hBboxLayout.addWidget(self.ShowMsgEdit)

        titleBar = TitleBar(self.mainwindow)
        titleBar.setTitle(u'已登录')
        titleBar.setLogo(':/darkqss/dark_img/undock.png')
        titleBar.connect(titleBar, QtCore.SIGNAL('maximaxProSignal'), self.maximizedOrNormal)

        vBoxLayout.addWidget(titleBar)
        # vBoxLayout.addWidget(self.menubar)
        vBoxLayout.addLayout(hBboxLayout)
        vBoxLayout.setAlignment(Qt.AlignTop)
        vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget.setLayout(vBoxLayout)

        # 处理右键打开，或者直接拖文件到桌面图标启动。
        # argv 参数大于1，说明有其他文件路径。第0位是当前应用程序，第1位则是我们需要处理的文件路径
        # 注意这里，是需要处理sys.argv 的编码问题的，方法是使用 WinCommandEnCoding.py 处理
        # if len(argv) > 1:
        #     filePath = argv[1]
        #     if SupportFiles.hasSupportFile(filePath):
        #         self.setLogTxt(_translate('', filePath, None))
        # 监听新到来的连接(新的终端被打开)
        self.localServer.connect(localServer, QtCore.SIGNAL('newConnection()'), self.newLocalSocketConnection)

        mainWindow.setCentralWidget(self.centralwidget)

    def minimized(self):
        pass

    def maximizedOrNormal(self):
        if self.mainwindow.isMaximized():
            self.mainwindow.showNormal()
        else:
            self.mainwindow.showMaximized()

    # 监听新到来的连接(新的终端被打开)
    def newLocalSocketConnection(self):
        # print 'newLocalSocketConnection'
        # 处理新启动的程序(终端)发过来的参数
        serverSocket = self.localServer.nextPendingConnection()
        if not serverSocket:
            return
        serverSocket.waitForReadyRead(1000)
        stream = QtCore.QTextStream(serverSocket)
        stream.setCodec('UTF-8')
        pathData = str(_translate('', stream.readAll(), None))
        serverSocket.close()
        # 由于客户端在发送的时候，就已经处理只发送(传递) 打开的文件路径参数，故此处不做校验处理
        # print SupportFiles.hasSupportFile(pathData)


class FFStoreMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        screen = QtGui.QDesktopWidget().screenGeometry()
        self.resize(screen.width() / 4 * 3, screen.height() / 4 * 3)
        # desktop = QDesktopWidget()
        # self.move((desktop.width() - self.width()) / 3, (desktop.height() - self.height()) / 0.85)
        # self.setWindowTitle(AppConstants.ApplicationName)
        # 初始化position
        self.mDragPosition = self.pos()
        # 设置顶级窗口, 无边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        # 边框圆角
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        # 显示托盘
        self.tray = TrayIcon(parent=self)
        self.tray.connect(self.tray, QtCore.SIGNAL('showProgramSignal'), self.showProgram)
        self.tray.show()
        self.tray.showMsg(u'FFStore 已启动, 请登录系统')

    def keyPressEvent(self, event):
        # 设置 "Ctrl+Q" 快捷键，用于程序
        if event.key() == QtCore.Qt.Key_Q and event.modifiers() == QtCore.Qt.ControlModifier:
            QtGui.QApplication.quit()

    # 支持窗口拖动,重写三个方法
    # https://www.cnblogs.com/codeAB/p/5019439.html
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mDrag = True
            self.mDragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.mDragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.mDrag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def showProgram(self):
        # print '---> isMaximized: %s, isMin: %s, isHide: %s, isVisible:%s , isActive: %s '\
        #       % (self.isMaximized(), self.isMinimized(), self.isHidden(), self.isVisible(), self.isActiveWindow())
        # 同时满足isMaximized和isMinimized 是因为最大化后，再缩小
        if self.isMaximized() and self.isMinimized():
            self.showMaximized()
        elif self.isMinimized():
            self.showNormal()
        else:
            return


class ShowWindowLogic:
    def __init__(self, **args):
        self.mainWindow = args['mainWindow']
        self.localServer = args['localServer']
        self.loginWindow = LoginWindow(self.mainWindow)
        self.uiMainWidget = Ui_MainWidget()

    def show(self):
        self.loginWindow.connect(self.loginWindow, QtCore.SIGNAL('loginStatusSignal(bool)'), self.loginCallBack)
        self.mainWindow.show()
        print self.loginWindow.leftVBoxLayout.geometry().width()
        print self.loginWindow.rightVBoxLayout.geometry().width()

    def loginCallBack(self, status):
        print 'loginStatus: %s' % status
        if status:
            self.loginWindow.close()
            self.uiMainWidget.setupUi(mainWindow=self.mainWindow, localServer=self.localServer)
            self.mainWindow.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ffstoreMainWin = FFStoreMainWindow()

    # set skin styleSheet
    # SkinHelper().setStyle(app, ':/qss/white_style.qss')
    SkinHelper().setStyle(app, ':/qss/dark_style.qss')

    # single QApplication solution
    # http://blog.csdn.net/softdzf/article/details/6704187
    serverName = 'FFStoreManagerServer'
    clientSocket = QLocalSocket()
    clientSocket.connectToServer(serverName)
    # 如果连接成功， 表明server 已经存在，当前已经有实例在运行, 将参数发送给服务端
    if clientSocket.waitForConnected(500):
        # print u'连接成功 arg = ', winOsArgv
        stream = QtCore.QTextStream(clientSocket)
        # for i in range(0, len(winOsArgv)):
        #     stream << winOsArgv[i]
        # 对于打开终端来说，所携带参数为第1位(打开文件的地址)，第0位为本执行程序地址
        # close client socket
        clientSocket.close()
        return app.quit()
    # 如果没有实例执行，创建服务器
    localServer = QLocalServer()
    # 一直监听端口
    localServer.listen(serverName)
    # 初始化全局变量
    GlobalVar.init()
    try:
        showWindowLogic = ShowWindowLogic(mainWindow=ffstoreMainWin, localServer=localServer)
        showWindowLogic.show()
        # uiMainWidget.setupUi(mainWindow=ffstoreMainWin, localServer=localServer)
        # ffstoreMainWin.show()
        sys.exit(app.exec_())
    finally:
        localServer.close()


if __name__ == '__main__':
    main()
