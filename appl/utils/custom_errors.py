# -*- coding: utf-8 -*-


class APIMessage:

    def __init__(self, result=None):
        self.result = result or 'success'

    def to_json(self):
        return self.__dict__


class APIWarning(Exception):

    def __init__(self, message, error_code=None):
        Exception.__init__(self, message)
        self.err_msg = message
        self.err_code = error_code or 0
