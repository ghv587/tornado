# __author__ = 'stone'
# #-*- coding: utf-8 -*-
# import os
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
# import pyrestful.rest
# from pyrestful import mediatypes
# from pyrestful.rest import get, post, put, delete
# import logging
# import torndb
#
#
# class Customer(object):
# def __init__(self,id_customer=0, name_customer=None, address_customer=None):
#     self.id_customer = id_customer
#     self.name_customer = name_customer
#     self.address_customer = address_customer
#
# # Setters
# def setId_Customer(self,id_customer):
#     self.id_customer = id_customer
# def setName_Customer(self,name_customer):
#     self.name_customer = name_customer
# def setAddress_Customer(self,address_customer):
#     self.address_customer = address_customer
#
# # Getters
# def getId_Customer(self):
#     return self.id_customer
# def getName_Customer(self):
#     return self.name_customer
# def getAddress_Customer(self):
#     return self.address_customer
#
# class CustomerDataBase(object):
# customerDB = dict()
# id_seq = 1
# def insert(self, name_customer, address_customer):
#     sequence = self.id_seq
#     customer = Customer(sequence, name_customer, address_customer)
#     self.customerDB[sequence] = customer
#     self.id_seq += 1
#     return sequence
#
# def update(self,id_customer, name_customer, address_customer):
#     if self.exists(id_customer):
#         customer = self.customerDB[id_customer]
#         customer.setName_Customer(name_customer)
#         customer.setAddress_Customer(address_customer)
#         self.customerDB[id_customer] = customer
#         return True
#     else:
#         return False
#
# def delete(self,id_customer):
#     if self.exists(id_customer):
#         del self.customerDB[id_customer]
#         return True
#     else:
#         return False
#
# def find(self,id_customer):
#     if self.exists(id_customer):
#         return self.customerDB[id_customer]
#     else:
#         return None
#
# def exists(self,id_customer):
#     if id_customer in self.customerDB:
#         return True
#     else:
#         return False
#
# class CustomerResource(pyrestful.rest.RestHandler):
# """
# a class for Customer Resource.
# """
# def initialize(self):
#     """
#     special initial for tornado.web.RequestHandler.
#     """
#     loggerRoot = logging.getLogger('root')
#     loggerRoot.debug("start CustomerResource module.")
#     self.database = CustomerDataBase()
#
# #REST-GET
# @get(_path="/customer/{id_customer}",_types=[int],_produces=mediatypes.APPLICATION_JSON)
# def getTest(self,id_customer):
#     try:
#         if not self.database.exists(id_customer):
#             self.gen_http_error(404,"Error 404 : do not exists the customer : %d"%id_customer)
#             return
#
#         customer = self.database.find(id_customer)
#
#         response = dict()
#         response['id_customer'] = customer.getId_Customer()
#         response['name_customer'] = customer.getName_Customer()
#         response['address_customer'] = customer.getAddress_Customer()
#         return response
#     except Exception,ex:
#         pass
#
# #REST-POST
# @post(_path="/customer", _types=[str,str], _produces=mediatypes.APPLICATION_JSON)
# def createCustomer(self, name_customer, address_customer):
#     try:
#         id_customer = self.database.insert(name_customer, address_customer)
#         return {"created_customer_id": id_customer}
#     except Exception,ex:
#         pass
#
# #REST-PUT
# @put(_path="/customer/{id_customer}", _types=[int,str,str], _produces=mediatypes.APPLICATION_JSON)
# def updateCustomer(self, id_customer, name_customer, address_customer):
#     try:
#         if not self.database.exists(id_customer):
#             self.gen_http_error(404,"Error 404 : do not exists the customer : %d"%id_customer)
#             return
#         updated = self.database.update(id_customer,name_customer,address_customer)
#         return {"updated_customer_id": id_customer, "success":updated}
#     except Exception,ex:
#         pass
#
# #REST-DELETE
# @delete(_path="/customer/{id_customer}", _types=[int], _produces=mediatypes.APPLICATION_JSON)
# def deleteCustomer(self,id_customer):
#     try:
#         if not self.database.exists(id_customer):
#             self.gen_http_error(404,"Error 404 : do not exists the customer : %d"%id_customer)
#             return
#         deleted = self.database.delete(id_customer)
#         return {"delete_customer_id": id_customer, "success":deleted}
#     except Exception,ex:
#         pass