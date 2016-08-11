import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.httpserver
import os
from tornado.options import define,options
import torndb
from define import *
import MySQLdb
from db import *
import logging
from monitor import *


class LoginHandle(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")


        db = torndb.Connection(user=options.mysql_user,
                               password=options.mysql_password,
                               host=options.mysql_host,
                               database=options.mysql_database, )
        sql = 'select * from user where username= %s and password= %s'
        db.query(sql, username, password)
        if  username != username:
            self.write("username wrong")
        elif password != password:
            self.write("password wrong")
        elif username != username and password != password:
            self.write("wrong")
        else:
            self.render('index.html')




class IndexHandle(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('index.html')





class WebApplication(tornado.web.Application):
    def __init__(self):
        handler = [
            (r"/index.html", IndexHandle),
            (r"/login.html", LoginHandle),
            (r"/", LoginHandle),
            (r"/monitor.html", MonitorHandle),
            # (r"/(.+?)\.(.+)",OtherHandle),

                   ]

        settings = {
            'template_path':os.path.join(os.path.dirname(__file__),'../template'),
            'static_path':os.path.join(os.path.dirname(__file__),'../static'),
            'debug': True,
            'login_url': '/login.html',
        }

        super(WebApplication, self).__init__(handler , **settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(WebApplication())
    http_server.listen(8888)
    options.parse_command_line()
    logging.debug("debug ...")
    tornado.ioloop.IOLoop.instance().start()


