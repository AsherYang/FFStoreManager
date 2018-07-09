#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/7/8
Desc:   后台首页   
"""

import StringIO
import os
import sys
import threading

from PyQt4 import QtCore, QtGui
from PyQt4.QtNetwork import QLocalServer, QLocalSocket
from constant import AppConstants

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
        self.menubar = QtGui.QMenuBar(mainWindow)

        adminLogin = self.menubar.addMenu(u' &登录')
        managerUser = self.menubar.addMenu(u'&用户管理')
        managerCate = self.menubar.addMenu(u'&分类管理')
        managerGoods = self.menubar.addMenu(u'&商品管理')
        managerOrder = self.menubar.addMenu(u'&订单管理')
        managerBanner = self.menubar.addMenu(u'&公告管理')
        managerOther = self.menubar.addMenu(u' &其他')

        # =============== action ======================
        # managerOther action
        otherExpressAction = QtGui.QAction(u'快递查询', mainWindow)
        otherExpressAction.setStatusTip(_fromUtf8('可根据快递单号或者订单号查询'))
        # otherExpressAction.connect(otherExpressAction, QtCore.SIGNAL('triggered()'), self.)
        otherBillAction = QtGui.QAction(u'账单统计', mainWindow)
        otherBillAction.setStatusTip(_fromUtf8('账单查询'))
        # =============== action ======================

        # =============== 控件 ======================
        self.ShowMsgEdit = QtGui.QTextEdit()
        self.ShowMsgEdit.setFont(self.getFont('Monospace'))
        self.ShowMsgEdit.setText(u'showMsgEdit')
        self.cateListWidget = QtGui.QListWidget()
        self.goodsListWidget = QtGui.QListWidget()
        # =============== 控件 ======================

        managerOther.addAction(otherExpressAction)
        managerOther.addAction(otherBillAction)

        # 添加到 mainWindow
        mainWindow.setMenuBar(self.menubar)
        mainWindow.setStatusBar(self.statusBar)

        # vBoxLayout 和 hBoxLayout 的选择依据是：根据2个控件的排列方向，上下排(vBoxLayout)还是左右排(hBoxLayout)
        vBoxLayout = QtGui.QVBoxLayout()
        hBboxLayout = QtGui.QHBoxLayout()

        hCateGoodsBoxLayout = QtGui.QHBoxLayout()
        hCateGoodsBoxLayout.addWidget(self.cateListWidget)
        hCateGoodsBoxLayout.addWidget(self.goodsListWidget)
        hCateGoodsBoxLayout.addWidget(self.ShowMsgEdit)

        hBboxLayout.addLayout(hCateGoodsBoxLayout)
        vBoxLayout.addLayout(hBboxLayout)
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

    def getFont(self, fontStr):
        font = QtGui.QFont()
        font.setFamily(fontStr)
        font.setPointSize(10)
        font.setFixedPitch(True)
        return font

    def showLoginDialog(self, filterList):
        if not filterList:
            return
        filterDialog = QtGui.QDialog()
        filterDialog.setWindowTitle(u'登陆')
        filterDialog.resize(260, 400)
        filterDialog.exec_()

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


class LogMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        screen = QtGui.QDesktopWidget().screenGeometry()
        self.resize(screen.width() / 4 * 3, screen.height() / 4 * 3)
        self.setWindowTitle(AppConstants.ApplicationName)
        self.setAcceptDrops(True)

    def keyPressEvent(self, event):
        # 设置 "Ctrl+w" 快捷键，用于关闭 tab
        if event.key() == QtCore.Qt.Key_W and event.modifiers() == QtCore.Qt.ControlModifier:
            self.emit(QtCore.SIGNAL('closeCurrentTabSignal()'))

    def dragEnterEvent(self, event):
        # http://www.iana.org/assignments/media-types/media-types.xhtml
        return

    # 和 dragEnterEvent 结合使用，处理拖拽文件进窗口区域，进行打开。与右键和拖文件到桌面图标打开方式不同。
    # 本方式是在窗口打开的前提下，直接拖文件到窗口上，这种方式打开。
    def dropEvent(self, event):
        return

    def closeCurrentTabSignal(self):
        return

    def dropOpenFileSignal(self, filePath):
        return


def main():
    app = QtGui.QApplication(sys.argv)
    logMainWin = LogMainWindow()
    uiMainWidget = Ui_MainWidget()
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
    try:
        uiMainWidget.setupUi(mainWindow=logMainWin, localServer=localServer)
        logMainWin.show()
        sys.exit(app.exec_())
    finally:
        localServer.close()


if __name__ == '__main__':
    main()
