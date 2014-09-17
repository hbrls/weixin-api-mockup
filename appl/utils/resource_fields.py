# -*- coding: utf-8 -*-
from flask.ext.restful import fields


class FieldsISO8601(fields.Raw):

    """
    Return a ISO 8601-formatted datetime string in UTC
    http://en.wikipedia.org/wiki/ISO_8601
    """

    def format(self, value):
        try:
            # value shall be instance of datetime.datetime
            return value.isoformat()
        except AttributeError as ae:
            raise fields.MarshallingException(ae)


class FieldsFloat(fields.Raw):

    """
    Return a js float
    """

    def format(self, value):
        try:
            return float(value)
        except ValueError as ve:
            raise fields.MarshallingException(ve)


class FieldsGravatarSmall(fields.Raw):
    def format(self, value):
        return 'http://www.gravatar.com/avatar/%s?s=32' % value
