from flask import Flask, jsonify, Blueprint
from flask_restful import Resource, Api

import models

class PostList(Resource):
    def get(self):
        return jsonify({'posts': [{'title': 'Python Basics'}]})

class Post(Resource):
    def get(self, id):
        return jsonify({'title': 'Python Basics'})

    def put(self, id):
        return jsonify({'title': 'Python Basics'})

    def delete(self, id):
        return jsonify({'title': 'Python Basics'})

posts_api = Blueprint('resources.posts', __name__)
api = Api(posts_api)
api.add_resource(
    PostList,
    '/api/v1/posts',
    endpoint='posts'
)
api.add_resource(
    Post,
    '/api/v1/posts/<int:id>',
    endpoint='post'
)