import tornado
import tornado.ioloop
import tornado.web
import tornado.websocket


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/ws", EchoWebSocket),
        ]
        settings = dict()
        super(Application, self).__init__(handlers, **settings)


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")


if __name__ == '__main__':
    app = Application()
    app.listen(address='0.0.0.0', port=8765)
    tornado.ioloop.IOLoop.current().start()