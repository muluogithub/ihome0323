import tornado.web
import json


class BaseHandler(tornado.web.RequestHandler):
    """基类"""
    def set_default_headers(self):
        pass

    def initialize(self):
        pass

    def prepare(self):
        content_type=self.request.headers.get('Content-Type')
        if content_type and content_type.startswith('application/json'):
            self.data_args=json.loads(self.request.body.decode())
        else:
            self.data_args={}


    def get(self):
        pass

    def post(self):
        pass

    @property
    def db(self):
        return self.application.db

    @property
    def redis(self):
        return self.application.redis