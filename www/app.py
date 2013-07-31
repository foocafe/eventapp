# -*- coding: utf-8 -*-

import json
import biz.models

from flask import Flask
from flask.ext.github import GitHub
from mongoengine import connect

# TODO: Some environment detection to swap the host
connect('foo_events', host='localhost', port=27017)

app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = '7202ee64b544e635bdbb'
app.config['GITHUB_CLIENT_SECRET'] = '9c0df971624cb42ec6c3b1ecda41b6c9927d1756'
app.config['GITHUB_CALLBACK_URL'] = 'http://localhost/auth/github-callback'

@app.route("/")
def hello():
    return "Hello World!"


# api methods for Event API - this is the initial version thus v1
@app.route('/api/v1/event_new', methods=['POST'])
def event_new():
    data = json.loads(request.data)
    FooEvent.objects.create()
    return "Hello World!"




# Authentication handler

@app.route('/auth/github-callback')
@github.authorized_handler
def authorized(oauth_token):
    next_url = request.args.get('next') or url_for('index')
    if oauth_token is None:
        flash("Authorization failed.")
        return redirect(next_url)

    user = FooUser.objects.get_or_create(oauth_data__email=)

    if user is None:
        user = User(token)

    user.github_access_token = oauth_token
    db_session.commit()
    return redirect(next_url)


if __name__ == "__main__":
    app.run()