#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/16
Desc  : adverts http, 广告 banner 网络操作
"""

from LoginHttp import LoginHttp
from constant import GlobalVar


class AdvertsHttp:
    def __init__(self):
        self.loginHttp = LoginHttp()
        pass

    def addAdvert(self):
        loginInfo = self.loginHttp.getLoginInfoDict()
        if loginInfo is None or loginInfo.keys() is None:
            print '----> login info is invalid.'
            return False
        else:
            user_tel = loginInfo.keys()[0]
            sms_pwd = loginInfo[user_tel]
            print user_tel
            print sms_pwd

    def deleteAdvert(self):
        pass


if __name__ == '__main__':
    advertsHttp = AdvertsHttp()
    advertsHttp.loginHttp.init_global()
    advertsHttp.loginHttp.login(user_tel=u'13553831061', sms_pwd='462251')
    advertsHttp.addAdvert()

