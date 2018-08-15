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
from net.NetGoodsSizeColor import NetGoodsSizeColor
from net.NetGoodsPhoto import NetGoodsPhoto
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
        # photo_thum_list
        goodsPhotoThumList = []
        if netGoods.goods_photos_thum_list:
            for photoThum in netGoods.goods_photos_thum_list:
                string = {'photos': photoThum.photo, 'thum_photo': photoThum.thum_photo}
                goodsPhotoThumList.append(string)
        # size_color_list
        goodsSizeColorList = []
        if netGoods.attr_size_color_list:
            for sizeColor in netGoods.attr_size_color_list:
                string = {'goodssize': sizeColor.attr_size, 'goodscolor': sizeColor.attr_color}
                goodsSizeColorList.append(string)
        params = {"tel": user_tel, "sms": sms_pwd, "cateid": netGoods.cate_id, "brandid": netGoods.brand_id,
                  "name": netGoods.goods_name, "marketprice": netGoods.market_price, "currentprice": netGoods.current_price,
                  "salecount": netGoods.sale_count, "stocknum": netGoods.stock_num, "status": netGoods.status,
                  "goodscode": netGoods.goods_code, "goodslogo": netGoods.goods_logo, "thumlogo": netGoods.thum_logo,
                  "keywords": netGoods.keywords, "photosthumlist": goodsPhotoThumList,
                  "marketyear": netGoods.attr_market_year, "sizecolorlist": goodsSizeColorList}
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

    def updateGoods(self, netGoods):
        loginInfo = self.loginHttp.getLoginInfoDict()
        if not netGoods:
            return False
        if loginInfo is None or loginInfo.keys() is None:
            return False
        user_tel = loginInfo.keys()[0]
        sms_pwd = loginInfo[user_tel]
        """
        goods_id = param['goodsid']
        cate_id = param['cateid']
        brand_id = param['brandid']
        goods_name = param['name']
        market_price = param['marketprice']
        current_price = param['currentprice']
        sale_count = param['salecount']
        stock_num = param['stocknum']
        status = param['status']
        goods_code = param['goodscode']
        goods_logo = param['goodslogo']
        thum_logo = param['thumlogo']
        keywords = param['keywords']

        goods_photos = param['photos']
        goods_thum_photo = param['thum_photo']
        attr_market_year = param['marketyear']
        attr_size = param['goodssize']
        attr_color = param['goodscolor']
        """
        # photo_thum_list
        goodsPhotoThumList = []
        if netGoods.goods_photos_thum_list:
            for photoThum in netGoods.goods_photos_thum_list:
                string = {'photos': photoThum.photo, 'thum_photo': photoThum.thum_photo}
                goodsPhotoThumList.append(string)
        # size_color_list
        goodsSizeColorList = []
        if netGoods.attr_size_color_list:
            for sizeColor in netGoods.attr_size_color_list:
                string = {'goodssize': sizeColor.attr_size, 'goodscolor': sizeColor.attr_color}
                goodsSizeColorList.append(string)
        params = {"tel": user_tel, "sms": sms_pwd, "goodsid": netGoods.goods_id, "cateid": netGoods.cate_id, "brandid": netGoods.brand_id,
                  "name": netGoods.goods_name, "marketprice": netGoods.market_price, "salecount": netGoods.sale_count,
                  "currentprice": netGoods.current_price, "stocknum": netGoods.stock_num, "status": netGoods.status,
                  "goodscode": netGoods.goods_code, "goodslogo": netGoods.goods_logo, "thumlogo": netGoods.thum_logo,
                  "keywords": netGoods.keywords, "photosthumlist": goodsPhotoThumList,
                  "marketyear": netGoods.attr_market_year, "sizecolorlist": goodsSizeColorList}
        body = HttpUtil.http_post(HttpApi.HOST_URl + HttpApi.URL_UPDATE_GOODS, params=params, header={})
        body = json.loads(body)
        print 'updateGoods: ', body
        if body['code'] == ResponseCode.op_success:
            print 'success: ', body['result']

if __name__ == '__main__':
    # 所有的接口都必须要求先进行登录
    goodsHttp = GoodsHttp()
    goodsHttp.loginHttp.init_global()
    goodsHttp.loginHttp.login(user_tel=u'13553831061', sms_pwd='778047')
    netGoods = NetGoods()
    netGoods.goods_id = '4117356719264239617'
    netGoods.cate_id = '4116946797280104449'
    netGoods.brand_id = '2222'
    netGoods.goods_name = u'限额3'
    netGoods.market_price = '180'
    netGoods.current_price = '20'
    netGoods.sale_count = 14
    netGoods.stock_num = 45
    netGoods.status = GoodsStatus.STATUS_ON_SALE
    # goods_code 唯一值限制
    netGoods.goods_code = '12344555'
    netGoods.keywords = u'鞋, 裤子, 红色'
    # photo
    photo_thum_list = []
    photoThum = NetGoodsPhoto()
    photoThum.photo = 'http://www.baidu.com'
    photoThum.thum_photo = 'http://www.qq.com'
    photoThum2 = NetGoodsPhoto()
    photoThum2.photo = 'http://www.google.com'
    photoThum2.thum_photo = 'http://www.weixin.com'
    photo_thum_list.append(photoThum)
    photo_thum_list.append(photoThum2)
    netGoods.goods_photos_thum_list = photo_thum_list
    netGoods.attr_market_year = '1983'
    # size_color
    size_color_list = []
    sizeColor = NetGoodsSizeColor()
    sizeColor.attr_size = 'xl'
    sizeColor.attr_color = '红'
    sizeColor2 = NetGoodsSizeColor()
    sizeColor2.attr_size = 'xxxl'
    sizeColor2.attr_color = '黑黑黑黑'
    sizeColor3 = NetGoodsSizeColor()
    sizeColor3.attr_size = 's'
    sizeColor3.attr_color = '白白白'
    size_color_list.append(sizeColor)
    size_color_list.append(sizeColor2)
    size_color_list.append(sizeColor3)
    netGoods.attr_size_color_list = size_color_list
    # goodsHttp.addGoods(netGoods)
    # goodsHttp.deleteGoods('4117356837128376321')
    # update ffstore_goods set goods_code = "12121", current_price = "110" where goods_id = "4117356719264239617";
    goodsHttp.updateGoods(netGoods)
