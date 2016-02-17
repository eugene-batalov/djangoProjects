#!/usr/bin/env python3
"""
WSGI config for gamepuzzleadmin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
import os, sys

from django.core.wsgi import get_wsgi_application
import pymysql
pymysql.install_as_MySQLdb()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gamepuzzleadmin.settings")

application = get_wsgi_application()
"""
def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
"""