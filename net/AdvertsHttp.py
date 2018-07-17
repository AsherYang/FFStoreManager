#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/16
Desc  : adverts http, 广告 banner 网络操作
"""

from util import HttpUtil
from net import HttpApi
from LoginHttp import LoginHttp
from constant import ResponseCode
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class AdvertsHttp:
    def __init__(self):
        self.loginHttp = LoginHttp()
        pass

    def addAdvert(self, cate_id, advert_title, advert_sort, advert_pic_url):
        loginInfo = self.loginHttp.getLoginInfoDict()
        if loginInfo is None or loginInfo.keys() is None:
            return False
        user_tel = loginInfo.keys()[0]
        sms_pwd = loginInfo[user_tel]
        params = {"tel": user_tel, "sms": sms_pwd, "cate_id": cate_id, "title": advert_title,
                  "sort": advert_sort, "pic_url": advert_pic_url}
        body = HttpUtil.http_post(HttpApi.HOST_URl + HttpApi.URL_ADD_ADVERT, params=params, header={})
        body = json.loads(body)
        print 'addAdvert: ', body
        if body['code'] == ResponseCode.op_success:
            print 'success: ', body['result']


    def deleteAdvert(self, advert_id):
        loginInfo = self.loginHttp.getLoginInfoDict()
        if loginInfo is None or loginInfo.keys() is None:
            return False
        user_tel = loginInfo.keys()[0]
        sms_pwd = loginInfo[user_tel]
        params = {"tel": user_tel, "sms": sms_pwd, "adverts_id": advert_id}
        body = HttpUtil.http_post(HttpApi.HOST_URl + HttpApi.URL_DELETE_ADVERT, params=params, header={})
        body = json.loads(body)
        print 'deleteAdvert: ', body
        if body['code'] == ResponseCode.op_success:
            print 'success: ', body['result']


if __name__ == '__main__':
    # 所有的接口都必须要求先进行登录
    advertsHttp = AdvertsHttp()
    advertsHttp.loginHttp.init_global()
    advertsHttp.loginHttp.login(user_tel=u'13553831061', sms_pwd='735431')
    advertsHttp.addAdvert(cate_id='4116840875748757505', advert_title=u"中华人民共和国万岁，万岁万万岁", advert_sort=1, advert_pic_url=u"http://www.baidu.com")
    # advertsHttp.deleteAdvert('12345')
