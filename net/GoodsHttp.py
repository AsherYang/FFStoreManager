#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/18
Desc  : 商品网络操作类
"""

from util import HttpUtil
from net import HttpApi
from net.NetGoods import NetGoods
from LoginHttp import LoginHttp
from constant import ResponseCode
from constant import GoodsStatus
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class GoodsHttp:
    def __init__(self):
        self.loginHttp = LoginHttp()

    def addGoods(self, netGoods):
        if not netGoods:
            return False
        loginInfo = self.loginHttp.getLoginInfoDict()
        if loginInfo is None or loginInfo.keys() is None:
            return False
        user_tel = loginInfo.keys()[0]
        sms_pwd = loginInfo[user_tel]
        params = {"tel": user_tel, "sms": sms_pwd, "cateid": netGoods.cate_id, "brandid": netGoods.brand_id,
                  "name": netGoods.goods_name, "marketprice": netGoods.market_price, "currentprice": netGoods.current_price,
                  "salecount": netGoods.sale_count, "stocknum": netGoods.stock_num, "status": netGoods.status,
                  "goodscode": netGoods.goods_code, "goodslogo": netGoods.goods_logo, "thumlogo": netGoods.thum_logo,
                  "keywords": netGoods.keywords}
        body = HttpUtil.http_post(HttpApi.HOST_URl + HttpApi.URL_ADD_GOODS, params=params, header={})
        body = json.loads(body)
        print 'addGoods: ', body
        if body['code'] == ResponseCode.op_success:
            print 'success: ', body['result']

    def deleteGoods(self, goods_id):
        loginInfo = self.loginHttp.getLoginInfoDict()
        if loginInfo is None or loginInfo.keys() is None:
            return False
        user_tel = loginInfo.keys()[0]
        sms_pwd = loginInfo[user_tel]
        params = {"tel": user_tel, "sms": sms_pwd, "goodsid": goods_id}
        body = HttpUtil.http_post(HttpApi.HOST_URl + HttpApi.URL_DELETE_GOODS, params=params, header={})
        body = json.loads(body)
        print 'deleteGoods: ', body
        if body['code'] == ResponseCode.op_success:
            print 'success: ', body['result']

    def updateGoods(self):
        pass

if __name__ == '__main__':
    # 所有的接口都必须要求先进行登录
    goodsHttp = GoodsHttp()
    goodsHttp.loginHttp.init_global()
    goodsHttp.loginHttp.login(user_tel=u'13553831061', sms_pwd='976083')
    netGoods = NetGoods()
    netGoods.cate_id = '4116842428933083133'
    netGoods.brand_id = '111111'
    netGoods.goods_name = u'限额'
    netGoods.market_price = '190'
    netGoods.current_price = '90'
    netGoods.sale_count = 13
    # netGoods.stock_num = 40
    netGoods.status = GoodsStatus.STATUS_ON_SALE
    # goods_code 唯一值限制
    netGoods.goods_code = '12342'
    netGoods.keywords = u'上衣, 裤子, 黑色'
    # goodsHttp.addGoods(netGoods)
    goodsHttp.deleteGoods('')
