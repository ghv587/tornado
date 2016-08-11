import tornado
import tornado.web

class MonitorHandle(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('monitor.html')
