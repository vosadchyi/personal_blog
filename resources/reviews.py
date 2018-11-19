
from flask import jsonify, Blueprint

from flask_restful import Resource, Api

import models

class ReviewList(Resource):
    def get(self):
        return jsonify({'reviews': [{'post': 1, 'rating': 5}]})

class Review(Resource):
    def get(self, id):
        return jsonify({'post': 1,'rating': 5})

    def put(self, id):
        return jsonify({'post': 1,'rating': 5})

    def delete(self, id):
        return jsonify({'post': 1,'rating': 5})

reviews_api = Blueprint('resources.reviews', __name__)
api = Api(reviews_api)
api.add_resource(
    ReviewList,
    '/reviews',
    endpoint='reviews'
)
api.add_resource(
    Review,
    '/reviews/<int:id>',
    endpoint='review'
)