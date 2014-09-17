# -*- coding: utf-8 -*-
from datetime import datetime
from flask.ext.login import current_user
from flask.ext.restful import Resource, fields, marshal_with
from appl.utils.resource_fields import FieldsISO8601, FieldsGravatarSmall


resource_fields_object = {
    'id': fields.Integer,
    'gravatar': FieldsGravatarSmall,
    'display_name': fields.String,
    'uri': fields.String,
}


resource_fields_activity = {
    'id': fields.Integer,
    'created': FieldsISO8601,
    'actor': fields.Nested(resource_fields_object),
    'object': fields.Nested(resource_fields_object),
    'target': fields.Nested(resource_fields_object),
    'action': fields.String,
}


class RFeeds(Resource):

    @marshal_with(resource_fields_activity)
    def get(self):
        records = [{
            'id': i,
            'created': datetime.utcnow(),
            'actor': current_user,
            'object': current_user,
            'target': current_user,
            'action': 'clean-create'
        } for i in range(10)]
        return records
