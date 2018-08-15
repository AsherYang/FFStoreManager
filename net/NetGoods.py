#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2018/7/18
Desc  : 商品goods网络传递数据
"""


class NetGoods:
    def __init__(self):
        self._goods_id = None
        self._cate_id = None
        self._brand_id = None
        self._goods_name = None
        self._market_price = None
        self._current_price = None
        self._sale_count = None
        self._stock_num = None
        self._status = None
        self._goods_code = None
        self._goods_logo = None
        self._thum_logo = None
        self._keywords = None
        self._goods_photos_thum_list = []
        self._attr_market_year = None
        self._attr_size_color_list = []

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value

    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value

    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value

    @property
    def market_price(self):
        return self._market_price

    @market_price.setter
    def market_price(self, value):
        self._market_price = value

    @property
    def current_price(self):
        return self._current_price

    @current_price.setter
    def current_price(self, value):
        self._current_price = value

    @property
    def sale_count(self):
        return self._sale_count

    @sale_count.setter
    def sale_count(self, value):
        self._sale_count = value

    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def goods_code(self):
        return self._goods_code

    @goods_code.setter
    def goods_code(self, value):
        self._goods_code = value

    @property
    def goods_logo(self):
        return self._goods_logo

    @goods_logo.setter
    def goods_logo(self, value):
        self._goods_logo = value

    @property
    def thum_logo(self):
        return self._thum_logo

    @thum_logo.setter
    def thum_logo(self, value):
        self._thum_logo = value

    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        self._keywords = value

    @property
    def goods_photos_thum_list(self):
        return self._goods_photos_thum_list

    @goods_photos_thum_list.setter
    def goods_photos_thum_list(self, value):
        self._goods_photos_thum_list = value

    @property
    def attr_market_year(self):
        return self._attr_market_year

    @attr_market_year.setter
    def attr_market_year(self, value):
        self._attr_market_year = value

    @property
    def attr_size_color_list(self):
        return self._attr_size_color_list

    @attr_size_color_list.setter
    def attr_size_color_list(self, value):
        self._attr_size_color_list = value
    #
    # def append(self, value):
    #     return self._attr_size_color_list + [value]
    #
    # # extend 只能是一个列表
    # def extend(self, value):
    #     return self._attr_size_color_list.extend(value)
