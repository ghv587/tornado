import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.httpserver
import os
from tornado.options import define,options
import torndb

define("mysql_host", default="127.0.0.1:3306", help="database host")
define("mysql_database", default="blog", help="database name")
define("mysql_user", default="root", help="database user")
define("mysql_password", default="123456", help="database password")



class LoginHandle(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

    # def post(self):
    #     # username = self.get_argument("username")
    #     # password = self.get_argument("password")
    #     # self.write("username")
    #     self.set_cookie('username',self.get_argument('username', None))
    #     self.render('home.html')
    #     # import pdb
    #     # pdb.set_trace()

class IndexHandle(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

class HomeHandle(tornado.web.RequestHandler):
    def get_current_user(self):
        user = self.get_cookie('username')
        return user


    def get(self, *args, **kwargs):
        # import pdb
        # pdb.set_trace()

        if not self.current_user:
            self.redirect("index.html")
            return
        self.render('home.html')


class WebApplication(tornado.web.Application):
    def __init__(self):
        handler = [
            (r"/index.html", IndexHandle),
            (r"/", LoginHandle),
            # (r"/(.+?)\.(.+)",OtherHandle),
            (r"/home.html", HomeHandle)
                   ]

        settings = {
            'template_path':os.path.join(os.path.dirname(__file__),'../template'),
            'static_path':os.path.join(os.path.dirname(__file__),'../static'),

        }

        super(WebApplication, self).__init__(handler , **settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(WebApplication())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
