import uvloop
from tornado.web import Application
import tornado.ioloop

from transport.routes import get_routes
from utils.logger import setting_logger

def make_app():
    return Application(get_routes())


if __name__ == "__main__":
    uvloop.install()
    setting_logger()
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
