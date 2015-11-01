# -*- coding: utf-8 -*-
import logging
from uuid import uuid4
from flask import Blueprint, render_template, current_app, jsonify, request


_logger = logging.getLogger(__name__)


mod = Blueprint('home', __name__, template_folder='templates')


@mod.route('/')
def index():
    _logger.debug('index debug')
    _logger.info('index info')
    _logger.warn('index warn')
    _logger.error('index error')

    return render_template('home/index.html')


@mod.route('/cgi-bin/token')
def token():
    """
    获取access token
    http://mp.weixin.qq.com/wiki/11/0e4b294685f817b95cbed85ba5e82b8f.html
    """

    grant_type = request.args.get('grant_type', None)
    if not grant_type:
        return jsonify({
            'errcode': 40014,
            'errmsg': '不合法的 grant_type'
        })

    appid = request.args.get('appid', None)
    if not appid:
        return jsonify({
            'errcode': 40014,
            'errmsg': '不合法的 appid'
        })

    secret = request.args.get('secret', None)
    if not secret:
        return jsonify({
            'errcode': 40014,
            'errmsg': '不合法的 secret'
        })

    _logger.info('success')

    return jsonify({
        'access_token': str(uuid4()),
        'expires_in': 7200,
    })
