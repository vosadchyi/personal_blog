from flask import Flask

import models
from resources.posts import posts_api
from resources.reviews import reviews_api

DEBUG = True
HOST = '127.0.0.1'
PORT = 8000

app = Flask(__name__)
app.register_blueprint(posts_api)
app.register_blueprint(reviews_api, url_prefix='/api/v1')

@app.route('/')
def hello():
    return 'Hello Vlad'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
