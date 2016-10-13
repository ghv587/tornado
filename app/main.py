#encoding:utf-8

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
# from monitor import MonitorHandle
from addhost import AddhostHandle
from utils.restapi.app import *
from app.utils.paracls.paramiko_class import *




class BaseHandle(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("username")




class LoginHandle(BaseHandle):
    def get(self):

        self.render('login.html')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        sql = 'select id from user where username=%s and password=%s'
        if db.get(sql, username, password) is None:
            return self.write(
                '''
                <script>
                    alert ("用户名或密码错误!")
                    window.location.href="/"
                </script>
                            ''')
        else:
            self.set_secure_cookie("username", self.get_argument("username"))  #"username"
            self.redirect('index')


class IndexHandle(BaseHandle):
    @tornado.web.authenticated
    def get(self, *args ,**kwargs):
        self.render('index.html')

class MonitorHandle(BaseHandle):
    @tornado.web.authenticated

    def get(self):
        self.render('func.html')

class OperfileHandle(BaseHandle):

    @tornado.web.authenticated

    def get(self):
        add = paramiko_exec('ls')
        self.render('operfile.html',add=add)


class LogoutHandle(BaseHandle):


    def get(self):
        self.clear_cookie("username")
        self.redirect("/")

class ApplicationHandle(BaseHandle):
    @tornado.web.authenticated

    def get(self):
        self.render('application.html')

class WebApplication(tornado.web.Application):
    def __init__(self):
        handler = [
            (r"/index", IndexHandle),
            (r"/login", LoginHandle),
            (r"/", IndexHandle),
            (r"/func", MonitorHandle ),
            (r"/func1", AddhostHandle),
            (r"/operfile", OperfileHandle),
            (r"/logout", LogoutHandle),
            (r"/application", ApplicationHandle),
            # (r"/(.+?)\.(.+)",OtherHandle)

                   ]

        settings = {
            'template_path':os.path.join(os.path.dirname(__file__),'../template'),
            'static_path':os.path.join(os.path.dirname(__file__),'../static'),
            'utils_path':os.path.join(os.path.dirname(__file__),'../utils'),
            'debug': True,
            'login_url': '/login',
            'cookie_secret': '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo='
        }

        super(WebApplication, self).__init__(handler , **settings)


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(WebApplication())
    http_server.listen(8888)

    options.parse_command_line()
    logging.debug("debug ...")
    tornado.ioloop.IOLoop.instance().start()


