#coding:utf-8

from define import *
import torndb
import MySQLdb


print 12123

db = torndb.Connection(user=options.mysql_user,
                       password=options.mysql_password,
                       host=options.mysql_host,
                       database=options.mysql_database, )

cre = 'create table blog(id int,content text)'
db.execute(cre)
string = 'wawuee'
exe = 'insert into blog(id,content)values(%d,"%s")' % (1, string)
db.execute(exe)






# sql =  'select * from user;'
# db.query(sql,'bbb',1)





# class dboperate():
#     def __init__(self,sql):
#         try:
#             db = torndb.Connection(user=options.mysql_user,
#                                    password=options.mysql_password,
#                                    host=options.mysql_host,
#                                    database=options.mysql_database, )
#             self.sql = sql
#             self.db = db
#         except Exception, e:
#             print '数据库连接失败!'



#
# data = torndb.Connection.query( 'select * from user;' )
# print data


