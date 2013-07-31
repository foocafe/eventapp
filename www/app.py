# -*- coding: utf-8 -*-

import json
from biz.models import *

from flask import Flask, request, url_for, flash
from flask.ext.restful import reqparse, abort, Api, Resource

from flask.ext.github import GitHub
from mongoengine import connect

# TODO: Some environment detection to swap the host
connect('foo_events', host='localhost', port=27017)

app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = '7202ee64b544e635bdbb'
app.config['GITHUB_CLIENT_SECRET'] = '9c0df971624cb42ec6c3b1ecda41b6c9927d1756'
app.config['GITHUB_CALLBACK_URL'] = 'http://localhost/auth/github-callback'


api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, )
parser.add_argument('sub_title', type=str)
parser.add_argument('description', type=str)
parser.add_argument('event_start', type=datetime, required=False)
parser.add_argument('event_end', type=datetime, required=False)
parser.add_argument('event_type', type=str, required=False)
parser.add_argument('category', type=str, default="Code", required=False)

class EventResourceCreator(Resource):

    def post(self):

        args = parser.parse_args()
        event = FooEvent.create(args['title'])

        event.sub_title = args['sub_title']
        event.description = args['description']

        event.save()
        return event.to_json(), 201

class EventResourceMutator(Resource):

    def get(self, event_id):
        return "Awsome", 200

    def put(self, event_id):
        event = FooEvent.objects(id=event_id)


    def delete(self, event_id):
        pass

# @app.route("/")
# def hello():
#     return "Hello World!"
#
#
# # api methods for Event API - this is the initial version thus v1
# @app.route('/api/v1/event', methods=['GET', 'PUT', 'POST', 'DELETE'])
# def event_new():
#     data = json.loads(request.data)
#     FooEvent.objects.create()
#     return "Hello World!"
#
#
#
#
# # Authentication handler
#
# @app.route('/auth/github-callback')
# @github.authorized_handler
# def authorized(oauth_token):
#     next_url = request.args.get('next') or url_for('index')
#     if oauth_token is None:
#         flash("Authorization failed.")
#         return redirect(next_url)
#
#     user = FooUser.objects.get_or_create(oauth_data__email=)
#
#     if user is None:
#         user = User(token)
#
#     user.github_access_token = oauth_token
#     db_session.commit()
#     return redirect(next_url)


api.add_resource(EventResourceCreator, "/api/v1/event")
api.add_resource(EventResourceMutator, "/api/v1/event/<int:event_id>")

if __name__ == "__main__":
    app.run(debug=True)