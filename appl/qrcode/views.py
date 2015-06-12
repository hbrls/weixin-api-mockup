# -*- coding: utf-8 -*-
import logging
from uuid import uuid4
from flask import Blueprint, request, current_app, jsonify


_logger = logging.getLogger(__name__)


mod = Blueprint('qrcode', __name__, template_folder='templates')



@mod.route('/cgi-bin/qrcode/create', methods=['POST'])
def create():
    """
    生成带参数的二维码
    http://mp.weixin.qq.com/wiki/18/28fc21e7ed87bec960651f0ce873ef8a.html
    """

    access_token = request.args.get('access_token', None)
    if not access_token:
        return jsonify({
            'errcode': 40014,
            'errmsg': '不合法的access_token'
        })

    command = request.get_json(force=True)

    # ** 这是在开发文档中找到的一个二维码，用微信去扫实际会提示“过期”
    return jsonify({
        'ticket': 'gQH47joAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL2taZ2Z3TVRtNzJXV1Brb3ZhYmJJAAIEZ23sUwMEmm3sUw==',
        'expire_seconds': command.get('expire_seconds'),
        'url':'http:\/\/weixin.qq.com\/q\/kZgfwMTm72WWPkovabbI'
    })
