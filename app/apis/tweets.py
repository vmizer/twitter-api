# app/apis/tweets.py
# pylint: disable=missing-docstring

from flask_restx import Namespace, Resource, fields
from app.db import tweet_repository

api = Namespace('tweets')

tweet = api.model('Tweet', {
    'id': fields.Integer,
    'text': fields.String,
    'created_at': fields.DateTime
})


@api.route('/<int:id>')
@api.param('id', 'The tweet unique identifier')
@api.response(404, 'Tweet not found')
class TweetResource(Resource):
    @api.marshal_with(tweet)
    def get(self, id):
        tweet_to_return = tweet_repository.get(id)
        if tweet_to_return is None:
            api.abort(404)
        else:
            return tweet_to_return