#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/7/13
Desc:   分类网络操作
"""

from util import HttpUtil
from net import HttpApi
from LoginHttp import LoginHttp
from constant import ResponseCode
import json


class CategoryHttp:
    def __init__(self):
        self.loginHttp = LoginHttp()

    def addCate(self, cate_name, cate_code, parent_code, show_type, cate_logo):
        loginInfo = self.loginHttp.getLoginInfoDict()
        if loginInfo is None or loginInfo.keys() is None:
            return False
        user_tel = loginInfo.keys()[0]
        sms_pwd = loginInfo[user_tel]
        params = {"tel": user_tel, "sms": sms_pwd, "catename": cate_name, "catecode": cate_code,
                  "parentcode": parent_code, "showtype": show_type, "catelogo": cate_logo}
        body = HttpUtil.http_post(HttpApi.HOST_URl + HttpApi.URL_ADD_CATE, params=params, header={})
        body = json.loads(body)
        print 'addCate: ', body
        if body['code'] == ResponseCode.op_success:
            print 'success: ', body['result']

    def deleteCate(self):
        pass

    def updateCate(self):
        pass


if __name__ == '__main__':
    # 所有的接口都必须要求先进行登录
    cateHttp = CategoryHttp()
    cateHttp.loginHttp.init_global()
    cateHttp.loginHttp.login(user_tel=u'13553831061', sms_pwd='735431')
    cateHttp.addCate(u'上衣', '13', '2', 1, 'http://www.baidu.com')
