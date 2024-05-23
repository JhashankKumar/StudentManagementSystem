import tornado.ioloop
import tornado.web
from handlers import SignupHandler, LoginHandler, ResultsHandler, ResultHandler

def make_app():
    return tornado.web.Application([
        (r"/signup", SignupHandler),
        (r"/login", LoginHandler),
        (r"/results", ResultsHandler),
        (r"/results/([0-9]+)", ResultHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
