# _*_ coding:utf-8 _*_
from wsgiref.simple_server import make_server
from wsgi import application

httpd=make_server('',8000,application)
print('Server HTTP on port 8000..')
httpd.serve_forever()