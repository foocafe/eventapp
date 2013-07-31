# -*- coding: utf-8 -*-

from biz.models import FooEvent
from flask.ext.restful import reqparse, abort, Resource
from datetime import datetime

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
        return "Awesome", 200

    def put(self, event_id):
        event = FooEvent.objects(id=event_id)


    def delete(self, event_id):
        pass
