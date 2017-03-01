from bottle import run, route, template

@route('/')
def index():
	return '<big>This is index page.</big>'
	
@route('/page')
def page():
	return template('hello', myList = ["Emma", "Jon", "David", "Robert", "Susan"])
	
run()
