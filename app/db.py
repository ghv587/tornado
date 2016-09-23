#coding:utf-8

from define import *
import torndb
import MySQLdb

# con = MySQLdb.Connection()


#
db = torndb.Connection(user=options.mysql_user,
                       password=options.mysql_password,
                       host=options.mysql_host,
                       database=options.mysql_database, )

# sql = 'select id from user where username=%s '
# print db.get(sql, 'bbb')
#
# if db.get(sql, 'bbb') is None:
#     print 1
# else:
#     print 2




# cre = 'create table blog(id int,content text)'
# db.execute(cre)
# string = 'wawuee'
# exe = 'insert into blog(id,content)values(%d,"%s")' % (1, string)
# db.execute(exe)



# select = 'select * from user where  username=%s  and password = %s'
# print db.query(select,'bbb', '123')




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


class db_operation(object):
    'MySQL的增删改查'
    def __init__(self,sql):
        try:
            db = torndb.Connection(user=options.mysql_user,
                                   password=options.mysql_password,
                                   host=options.mysql_host,
                                   database=options.mysql_database, )
            self.sql = sql
            self.db = db
        except Exception,e:
            print '数据库连接失败!'

    def select(self):
        try:
            select_data = self.db.query(self.sql)
            return select_data
        except Exception,e:
            print self.sql
            print 'SQL 语法有问题!'
        finally:
            self.db.close()

    def update(self):
        try:
            update_data = self.db.execute(self.sql)
            return update_data
        except Exception,e:
            print self.sql
	    print 'SQL 语法有问题!'
	finally:
	    self.db.close()

    def delete(self):
        try:
	    delete_data = self.db.execute(self.sql)
	    return delete_data
	except Exception,e:
	    print self.sql
	    print 'SQL 语法有问题!'
	finally:
	    self.db.close()



