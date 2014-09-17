from functools import update_wrapper
from datetime import timedelta
from flask import Response, request, make_response, current_app
import json


def to_json():
    def decorator(f):
        def wrapped_function(*args, **kwargs):
            r = json.dumps(f(*args, **kwargs))
            res = Response(r, status=200, mimetype='application/json')
            return res

        return update_wrapper(wrapped_function, f)

    return decorator


def to_xml():
    def decorator(f):
        def wrapped_function(*args, **kwargs):
            res = Response(f(*args, **kwargs), status=200, mimetype='text/xml')
            return res

        return update_wrapper(wrapped_function, f)

    return decorator

# http://flask.pocoo.org/mailinglist/archive/2011/8/8/add-no-cache-to-response/#952cc027cf22800312168250e59bade4


def never_cache(f):
    def wrapped_function(*args, **kwargs):
        res = Response(f(*args, **kwargs))
        res.headers['Cache-Control'] = 'no-cache'
        return res
    return update_wrapper(wrapped_function, f)


# http://flask.pocoo.org/snippets/56/
def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)

            # http://stackoverflow.com/a/7556908/707580
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers

            return resp

        f.provide_automatic_options = False
        # http://flask.pocoo.org/snippets/56/#Comments[0]
        f.required_methods = ['OPTIONS']

        return update_wrapper(wrapped_function, f)

    return decorator
