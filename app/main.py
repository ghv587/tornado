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
from monitor import MonitorHandle
from addhost import AddhostHandle
from utils.restapi.app import *

class BaseHandle(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_cookie("username")

    # @tornado.web.authenticated
    # def get(self):
    #     if not self.current_user:
    #         self.redirect('login.html')
    #         return




class LoginHandle(BaseHandle):
    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self,*args, **kwargs):
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
            self.set_cookie(username, self.get_argument("username"))
            self.render('index.html')
            # return self.write(self.get_secure_cookie('username'))



        # if  username != 'ee':
        #     return self.write(
        #         '''
        #         <script>
        #             alert ("用户名或密码错误!")
        #             window.location.href="/"
        #         </script>
        #                     ''')
        # elif password != '444':
        #     return self.write('''<script>
        #                     alert ("用户名或密码错误!")
        #     	        window.location.href="/"
        #     		</script>
        #                 ''')
        # elif username != username and password != password:
        #     return self.write('''<script>
        #                     alert ("用户名或密码错误!")
        #     	        window.location.href="/"
        #     		</script>
        #                 ''')
        # else:
        #     self.render('index.html')




class IndexHandle(BaseHandle):
    # @tornado.web.authenticated
    def get(self, *args ,**kwargs):
        self.render('index.html', user=self.current_user)




class WebApplication(tornado.web.Application):
    def __init__(self):
        handler = [
            (r"/index.html", IndexHandle),
            (r"/login.html", LoginHandle),
            (r"/", LoginHandle),
            (r"/func.html", MonitorHandle),
            (r"/func1.html", AddhostHandle),
            # (r"/(.+?)\.(.+)",OtherHandle),

                   ]

        settings = {
            'template_path':os.path.join(os.path.dirname(__file__),'../template'),
            'static_path':os.path.join(os.path.dirname(__file__),'../static'),
            'utils_path':os.path.join(os.path.dirname(__file__),'../utils'),
            'debug': True,
            'login_url': '/login.html',
            # 'cookie_secret': "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="
        }

        super(WebApplication, self).__init__(handler , **settings)




if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(WebApplication())
    http_server.listen(8888)

    options.parse_command_line()
    logging.debug("debug ...")
    tornado.ioloop.IOLoop.instance().start()


