import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.httpserver
import os

class IndexHandle(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('../template/index.html')


class WebApplication(tornado.web.Application):
    def __init__(self):
        handler = [
            (r"/", IndexHandle),
                    ]
        super(WebApplication, self).__init__(handler)

        settings = {
            'template_path':os.path.join(os.path.dirname(__file__),'template'),
            'static_path':os.path.join(os.path.dirname(__file__),'static')

        }



if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(WebApplication())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
