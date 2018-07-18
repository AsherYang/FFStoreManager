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
from constant.CategoryShowType import *
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

    def deleteCate(self, cate_id):
        loginInfo = self.loginHttp.getLoginInfoDict()
        if loginInfo is None or loginInfo.keys() is None:
            return False
        user_tel = loginInfo.keys()[0]
        sms_pwd = loginInfo[user_tel]
        params = {"tel": user_tel, "sms": sms_pwd, "cate_id": cate_id}
        body = HttpUtil.http_post(HttpApi.HOST_URl + HttpApi.URL_DELETE_CATE, params=params, header={})
        body = json.loads(body)
        print 'deleteCate: ', body
        if body['code'] == ResponseCode.op_success:
            print 'success: ', body['result']

    def updateByCateCode(self, cate_code, parent_code, cate_name, cate_logo, show_type=TYPE_SHOW_NORMAL):
        loginInfo = self.loginHttp.getLoginInfoDict()
        if loginInfo is None or loginInfo.keys() is None:
            return False
        user_tel = loginInfo.keys()[0]
        sms_pwd = loginInfo[user_tel]
        params = {"tel": user_tel, "sms": sms_pwd, "catecode": cate_code, "parentcode": parent_code,
                  "catename": cate_name, "catelogo": cate_logo, "showtype": show_type}
        body = HttpUtil.http_post(HttpApi.HOST_URl + HttpApi.URL_UPDATE_CATE, params=params, header={})
        body = json.loads(body)
        print 'updateCate: ', body
        if body['code'] == ResponseCode.op_success:
            print 'success: ', body['result']


if __name__ == '__main__':
    # 所有的接口都必须要求先进行登录
    cateHttp = CategoryHttp()
    cateHttp.loginHttp.init_global()
    cateHttp.loginHttp.login(user_tel=u'13553831061', sms_pwd='735431')
    # cateHttp.addCate(u'上衣', '123456', '237', 4, 'http://www.baidu.com')
    cateHttp.deleteCate('4117112222009790465')
    # cateHttp.updateByCateCode(cate_code='12345', parent_code=3333, cate_name='裤子3', cate_logo='http://www.oyf.name')
