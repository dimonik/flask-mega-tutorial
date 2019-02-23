from app import fapp

@fapp.route('/')
@fapp.route('/index')
def index():
	return "<H1 style=\"color: #4ce0b3\">The Future is Here!</H1><img src=\"/static/images/rocket.jpg\" width=\"631\" height=\"250\">"
