# урок по статье
# https://habr.com/ru/post/346306/

from flask import Flask

fapp = Flask(__name__, static_url_path='/static')

from app import routes
