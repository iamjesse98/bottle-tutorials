from bottle import run, route

@route('/')
def index():
	return '<h5>Hello</h5>'

@route('/jesse')
def jesse():
	return '<h2>Welcome to Jesse\'s page</h2>'
	
run(debug = True, reload = True)
