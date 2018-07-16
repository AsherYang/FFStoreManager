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
from constant import ResponseCode
import json


class LoginHttp:
    def __init__(self):
        # 本地登录状态
        self.LocalLoginState = False

    def login(self, user_tel, sms_pwd):
        params = {"tel": user_tel, "sms": sms_pwd}
        # header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        body = HttpUtil.http_post(HttpApi.HOST_URl+HttpApi.URL_LOGIN, params=params, header={})
        print 'login: ', json.loads(body)
        if body['code'] == ResponseCode.op_success:
            print 'success: ', str(body['result'])
            pass

    def logout(self):
        pass
    """
    获取登陆状态
    前端只保存登陆状态，后端做登陆校验
    1. 在登陆后，全局范围保存登陆信息
    2. 保存的全局登陆信息为字典形式: loginState:{MD5(tel): time}, 手机号和超时时间，若不存在手机号，或者时间为空或者超时，都判断为无效登陆信息
    3. 其中接口传递手机号是以 MD5 形式传递
    3. 后面其他接口获取登陆信息。而不必重复查询数据库
    """
    def getLocalLoginState(self):
        return self.LocalLoginState


if __name__ == '__main__':
    loginHttp = LoginHttp()
    loginHttp.login(user_tel=u'13553831061', sms_pwd='462251')
