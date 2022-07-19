# !/usr/bin/env python
# -*-coding:utf-8 -*-

from django.db import models


# Create your models here.
# class Users(models.Model):
#     """
#     用户表
#     """
#
#     username = models.CharField('用户名')
#     password = models.CharField('密码')
#     name = models.CharField('姓名')
#
#
# class Position(models.Model):
#     """
#     职位表
#     """
#
#     position = models.CharField('职位名')
#
#
# class Materials(models.Model):
#     """
#     材料表
#     """
#
#     name = models.CharField('材料名')
#     unit = models.CharField('材料单位')
#
#
# class MaterialPurchase(models.Model):
#     """
#     材料进货表
#     """
#
#     price = models.IntegerField('进货单价')
#     num = models.IntegerField('进货数量')
#     date = models.DateTimeField('进货日期')
#     materials_id = models.ForeignKey('Materials', on_delete=models.CASCADE)
#
#
# class MaterialStock(models.Model):
#     """
#     材料库存
#     """
#
#     num = models.IntegerField('材料库存数')
#     materials_id = models.ForeignKey('Materials', on_delete=models.CASCADE)
#
#
# class MaterialDelivery(models.Model):
#     """
#     材料出库
#     """
#
#     num = models.IntegerField('材料出库数')
#     date = models.DateTimeField('出库日期')
#     materials_id = models.ForeignKey('Materials', on_delete=models.CASCADE)
#
#
# class Product(models.Model):
#     """
#     成品表
#     """
#
#     name = models.CharField('成品名称')
#     unit = models.CharField('成品单位')
#
#
# class ProductStorage(models.Model):
#     """
#     成品入库
#     """
#
#     num = models.IntegerField('入库数量')
#     date = models.DateTimeField('入库日期')
#     Product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
#
#
# class ProductStock(models.Model):
#     """
#     成品库存
#     """
#
#     num = models.IntegerField('成品库存数')
#     Product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
#
#
# class ProductDelivery(models.Model):
#     """
#     成品出库
#     """
#
#     num = models.IntegerField('成品出库数')
#     date = models.DateTimeField('出库日期')
#     price = models.IntegerField('出库单价')
#     Product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
