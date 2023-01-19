from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Hello!'


application.run(host='0.0.0.0', port=81)