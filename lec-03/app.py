from bottle import run, route, template

@route('/')
def index():
	return '<h3>You are on index page</h3>'
	
@route('/jesse')
def jesse():
	return template('jesse', name = 'Jesse')
	
run(debug = True, reloader = True)
