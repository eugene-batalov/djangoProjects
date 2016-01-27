"""
WSGI config for gamepuzzleadmin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/


import os, sys

from django.core.wsgi import get_wsgi_application


sys.path.append('/anaconda/lib/python3.5/site-packages/django/')
sys.path.append('/Home/galinabatalova/pythonProjects/')
sys.path.append('/anaconda/bin/')
sys.path.append('/anaconda/lib/python3.5/')

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
