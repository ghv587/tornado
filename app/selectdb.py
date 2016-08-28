import paramiko
import tornado
import tornado.web
import pyrestful.rest
from pyrestful.rest import put, get, post ,delete
from pyrestful import mediatypes
import torndb
from torndb import *

class Selectdb(pyrestful.rest):
    # @get(
    #     select =
    # )
    # def method(self,id):
    #     return config(func, 'GET', **kwparams)  # 1.需要执行的方法，2.method， 3.参数
    #
    # def get(*params, **kwparams):
    #     """ Decorator for config a python function like a Rest GET verb	"""
    #     sql = 'select id from user where bbb and password=123'
    #     db.get(sql, username, password)
    #
    #
    #     def method(func):
    #         return config(func, 'GET', **kwparams)  # 1.需要执行的方法，2.method， 3.参数
    #
    #     return method



