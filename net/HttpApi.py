#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Author: AsherYang
Email:  ouyangfan1991@gmail.com
Date:   2018/7/14
Desc:   http API   
"""

HOST_URl = 'https://ffstore.oyfstore.com'

# 登录URL
URL_LOGIN = '/manager/admin/login'
# 添加广告 banner
URL_ADD_ADVERT = '/manager/adverts/add'
# 删除广告 banner
URL_DELETE_ADVERT = '/manager/adverts/delete'
# 添加分类URL
URL_ADD_CATE = '/manager/cate/add'
# 删除分类(以及商品)
URL_DELETE_CATE = '/manager/cate/delete/goods'
# 更新分类
URL_UPDATE_CATE = '/manager/cate/update'
# 添加商品
URL_ADD_GOODS = '/manager/goods/add'
# 删除商品
URL_DELETE_GOODS = '/manager/goods/delete'
# 更新商品
URL_UPDATE_GOODS = '/manager/goods/update'
