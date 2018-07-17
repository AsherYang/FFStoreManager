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
from constant import GlobalVar


class LoginHttp:
    def __init__(self):
        self.global_key_tel = 'login_tel'
        self.global_value_pwd = 'login_pwd'

    def login(self, user_tel, sms_pwd):
        params = {"tel": user_tel, "sms": sms_pwd}
        # header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        body = HttpUtil.http_post(HttpApi.HOST_URl+HttpApi.URL_LOGIN, params=params, header={})
        body = json.loads(body)
        print 'login: ', body
        # print type(body)
        if body['code'] == ResponseCode.op_success:
            print 'success: ', body['result']
            # save login info dict
            GlobalVar.setValue(self.global_key_tel, user_tel)
            GlobalVar.setValue(self.global_value_pwd, sms_pwd)

    def logout(self):
        GlobalVar.setValue(self.global_key_tel, None)
        GlobalVar.setValue(self.global_value_pwd, None)

    """
    获取登陆信息
    用于后面访问接口，直接获取登录信息
    登录成功，则返回字典形式{tel:sms_pwd}，否则返回 None
    便于后端做登录校验GlobalVar.init()
    @:return {tel:sms_pwd}
    """
    def getLoginInfoDict(self):
        tel = GlobalVar.getValue(self.global_key_tel)
        pwd = GlobalVar.getValue(self.global_value_pwd)
        if tel is None or pwd is None:
            return None
        return {tel: pwd}

    # 便于测试接口, 正式环境,在FFStoreManager#main()方法进行
    def init_global(self):
        GlobalVar.init()


if __name__ == '__main__':
    loginHttp = LoginHttp()
    loginHttp.init_global()
    loginHttp.login(user_tel=u'13553831061', sms_pwd='462251')
    print loginHttp.getLoginInfoDict()
