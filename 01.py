import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import config
import urls
import torndb
import redis


tornado.options.define(name='port',default=5566,type=int,help='run server on this port')


# 数据库初始化
class Application(tornado.web.Application):
    def __init__(self,*args,**kwargs):
        headers=urls.headers
        super(Application,self).__init__(headers,**config.settings)
        self.db=torndb.Connection(**config.mysql_config)
        self.redis=redis.StrictRedis(**config.redis_config)


def main():
    tornado.options.parse_command_line()
    app=Application()
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()



