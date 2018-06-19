# _*_ coding:utf-8 _*_
def application(eviron,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	body='<h1>Hello,%s!</h1>' % (eviron['PATH_INFO'][1:]or'web')
	return [body.encode('utf-8')]