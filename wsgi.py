# -*- coding: utf-8 -*-
def application(environ, start_response):
    status = '200 OK' # HTTP Status
    headers = [('Content-type', 'text/plain')] # HTTP Headers
    start_response(status, headers)

    # The returned object is going to be printed
    return ["Hello World"]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('', 8080, application)
    print "Serving on port 8080 ..."

    # Serve until process is killed
    httpd.serve_forever()
