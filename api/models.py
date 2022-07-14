# !/usr/bin/env python
# -*-coding:utf-8 -*-

from django.db import models

class Users(models.Model):
    """
    用户表
    """

    username = models.CharField('用户名')
    password = models.CharField('密码')
    name = models.CharField('姓名')
