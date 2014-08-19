#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from flask import Blueprint
from flask import request
from flask import make_response

api = Blueprint('api', __name__)

from models import Friend
from app import db


def make_json_response(content, statuscode):
    resp = make_response(json.dumps(content), statuscode)
    resp.headers['Content-Type'] = 'application/json'
    return resp


@api.route('/friends', methods=['GET', 'POST'])
def hotspots_handler():
    if request.method == 'GET':
        friends = Friend.query.\
            all()
        return make_json_response([f.to_json() for f in friends], 200)

    if request.method == 'POST':
        data = request.json
        f = Friend()
        f.name = data.get('name')
        f.birthday = data.get('birthday')
        f.height = data.get('height')
        f.image_url = data.get('image_url')
        f.notes = data.get('notes')
        f.is_special = data.get('is_special')
        db.session.add(f)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return make_json_response({'error': 'failed'}, 400)
        return make_json_response(f.to_json(), 200)


@api.route('/friends/<int:friend_id>', methods=['DELETE'])
def hotspot_handler(friend_id):
    if request.method == 'DELETE':
        friend = Friend.query.get_or_404(friend_id)
        db.session.delete(friend)
        db.session.commit()
        return make_json_response({}, 204)
