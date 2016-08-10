import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import tornado.options
import tornado.ioloop
import tornado.web
import tornado.template
import tornado.auth
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "./html/"),
    "cookie_secret": "--------------------------------------------",
    "debug": True,
}
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish("Hello PySelenium!")
class EnvHandler(tornado.web.RequestHandler):
    def get(self):
        html = "System Environment:\n\n<br>"
        for env in os.environ.keys():
          html += env + ': ' + os.environ[env] + "\n<br>"
        self.write(html)
application = tornado.web.Application([
    (r"/env", EnvHandler),
    (r"/()$", tornado.web.StaticFileHandler, {'path':'html/Pyselenium.html'}),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path':'html/'}),
    (r"/.*", MainHandler),
    ], **settings)
if __name__ == "__main__":
    tornado.options.define("port", default=8000, help="Run server on a specific port", type=int)
    tornado.options.parse_command_line()
    application.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()