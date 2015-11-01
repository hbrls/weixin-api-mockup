# -*- coding: utf-8 -*-
import logging
from flask import Flask, render_template, request, jsonify
# from flask.ext.sqlalchemy import get_debug_queries
# from .extensions import db


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_object('appl.configs.default.DefaultConfig')
    app.config.from_object(config)

    configure_logging(app)
    # configure_extensions(app)
    configure_blueprints(app)

    from .template_filters import configure_template_filters
    configure_template_filters(app)

    # from .restful_apis import configure_apis
    # configure_apis(app)

    configure_error_handlers(app)

    return app


def configure_logging(app):
    if app.debug:
        return

    formatter = '%(asctime)s %(levelname)s %(name)s (%(lineno)s) %(message)s'
    logging.basicConfig(format=formatter)

    base_logger = logging.getLogger('appl')
    base_logger.setLevel(logging.DEBUG)


# def configure_extensions(app):
    # # Flask-SQLAlchemy
    # db.init_app(app)

    # @app.teardown_appcontext
    # def slow_queries(error):
    #     for query in get_debug_queries():
    #         if query.duration >= 0.5:
    #             warning_message = """
    #             SLOW QUERY: %s
    #             Parameters: %s
    #             Duration: %fs
    #             Context: %s
    #             """ % (query.statement,
    #                    query.parameters,
    #                    query.duration,
    #                    query.context)
    #             app.logger.warning(warning_message)


def configure_blueprints(app):
    # from auth.views import mod as auth_views
    # app.register_blueprint(auth_views)

    # from account.views import mod as account_views
    # app.register_blueprint(account_views, url_prefix='/accounts')

    from .home.views import mod as home_views
    app.register_blueprint(home_views)

    from .qrcode.views import mod as qrcode_views
    app.register_blueprint(qrcode_views)

    from .jssdk.views import mod as jssdk_views
    app.register_blueprint(jssdk_views)

    # from user.views import mod as user_views
    # app.register_blueprint(user_views, url_prefix='/users')


def configure_error_handlers(app):
    @app.errorhandler(403)
    def ERROR403(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def ERROR404(e):
        app.logger.warn('404: %s, %s, %s' % (request.url,
                                                request.remote_addr,
                                                request.user_agent.string))

        app.logger.warn(request.args)
        app.logger.warn(request.get_json(force=True, silent=True))

        return jsonify({
            'errcode': 48001,
            'errmsg': 'The API is not mocked yet.',
        }), 404

    @app.errorhandler(500)
    def ERROR500(e):
        # ** Flask will by default call app.logger.error
        return render_template('errors/500.html', error=unicode(e)), 500
