#!/usr/bin/env python

import json
import socket
import web

urls = ('/',         'Default',
        '/api/(.*)', 'Api')

class Default:
    def GET(self):
        web.header('Content-Type', 'text/html')
        hostname = socket.gethostname()
        return """<html>
        <title>Hello World!</title>
        <body bgcolor="white">
        <h1>Farnaz</h1>
        <p>Available API methods:</p>
        <ul>
        <li><a href="/api/v1/test">/api/v1/test</a></li>
        <li><a href="/api/v1/json">/api/v1/json</a></li>
        <li><a href="/api/v1/worker">/api/v1/worker</a></li>
        </ul>
        <em>{}</em>
        </body>
        </html>""".format(hostname)

class Api:
    def GET(self, name):
        if name == 'v1/test':
            return self.test()
        elif name == 'v1/json':
            return self.json()
        elif name == 'v1/worker':
            return self.worker()
        else:
            web.header('Content-Type', 'text/html')
            web.ctx.status = '404 Not Found'
            return "undefined"
    def test(self):
        web.header('Content-Type', 'application/json')
        return json.dumps({'test': True})
    def json(self):
        web.header('Content-Type', 'application/json')
        return json.dumps({'api-version': 'v1', 'app-name': 'pywebapp'})
    def worker(self):
        web.header('Content-Type', 'application/json')
        hostname = socket.gethostname()
        return json.dumps({'worker-name': hostname})

web.config.debug = False
app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()

# vim:ai ts=4 sw=4 et:
