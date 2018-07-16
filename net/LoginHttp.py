#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/7/14
Desc:   登录网路操作
"""

from util import HttpUtil
from net import HttpApi


class LoginHttp:
    def __init__(self):
        # 本地登录状态
        self.LocalLoginState = False

    def login(self, user_tel, sms_pwd):
        params = {"tel": user_tel, "sms": sms_pwd}
        # header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        body = HttpUtil.http_post(HttpApi.HOST_URl+HttpApi.URL_LOGIN, params=params, header={})
        print 'login: ', body
        pass

    def logout(self):
        pass

    def getLocalLoginState(self):
        return self.LocalLoginState


if __name__ == '__main__':
    loginHttp = LoginHttp()
    loginHttp.login(user_tel=u'13553831061', sms_pwd='462251')
