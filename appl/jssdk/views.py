# -*- coding: utf-8 -*-
import logging
from uuid import uuid4
from flask import Blueprint, request, current_app, jsonify


_logger = logging.getLogger(__name__)


mod = Blueprint('jssdk', __name__, template_folder='templates')



@mod.route('/cgi-bin/ticket/getticket', methods=['GET'])
def getticket():
    """
    获取 jsapi_ticket
    http://mp.weixin.qq.com/wiki/7/aaa137b55fb2e0456bf8dd9148dd613f.html#.E9.99.84.E5.BD.951-JS-SDK.E4.BD.BF.E7.94.A8.E6.9D.83.E9.99.90.E7.AD.BE.E5.90.8D.E7.AE.97.E6.B3.95
    """

    access_token = request.args.get('access_token', None)
    if not access_token:
        return jsonify({
            'errcode': 40014,
            'errmsg': '不合法的 access_token'
        })

    auth_type = request.args.get('type', None)
    if not auth_type or auth_type != 'jsapi':
        return jsonify({
            'errcode': 40014,
            'errmsg': '不合法的 type'
        })

    return jsonify({
        'errcode': 0,
        'errmsg': 'ok',
        'ticket': 'FAKE_JSAPI_TICKET',
        'expires_in': 7200,
    })
