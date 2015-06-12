# -*- coding: utf-8 -*-
import logging
from uuid import uuid4
from flask import Blueprint, render_template, current_app, jsonify


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
    return jsonify({
        'access_token': str(uuid4()),
        'expires_in': 7200,
    })
