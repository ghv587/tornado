import tornado
import tornado.web
from main import BaseHandle
from tornado import escape

class MonitorHandle(BaseHandle):
    # @tornado.web.authenticated
    def get(self):
        # self.current_user = self.get_secure_cookie
        # if not self.current_user:
        #     self.redirect('login.html')
        #     return
        self.render('func.html')
        # self.render('monitor.html', user=self.current_user)


    # @tornado.web.authenticated
    # def get(self, *args, **kwargs):
    #     if  self.get_current_user():
    #         self.render('login.html')
    #         return
    #     self.redirect('monitor.html')

    # def get(self, *args, **kwargs):
    #     return self.write(self.get_secure_cookie('username'))