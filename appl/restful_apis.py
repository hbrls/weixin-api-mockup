# -*- coding: utf-8 -*-
from flask.ext.restful import Api
from appl.utils.custom_errors import APIWarning
from appl.activity_stream.resources import RFeeds


class ExceptionAwareApi(Api):
    def handle_error(self, e):
        if isinstance(e, APIWarning):
            return self.make_response(e.__dict__, 200)
        else:
            return super(ExceptionAwareApi, self).handle_error(e)


def configure_apis(app):
    api = ExceptionAwareApi(app, prefix='/api')
    # print app.view_functions

    api.add_resource(RFeeds, '/r_feeds', endpoint='api.r_feeds')
    app.add_url_rule('/api/feeds', 'api.r_feeds', methods=['GET'])
