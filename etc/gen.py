# -*- coding: utf-8 -*-
import os
from string import Template


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def gen_conf(tpl, conf, **kwargs):
    tpl = os.path.join(CURRENT_DIR, tpl)
    conf = os.path.join(CURRENT_DIR, conf)
    with open(tpl) as f_tpl, open(conf, 'w') as f_conf:
        t = Template(f_tpl.read())
        c = t.substitute(kwargs)
        f_conf.write(c)


gen_conf('./uwsgi.example.yaml', './uwsgi.yaml', name='probe.42smart.com')

gen_conf('./nginx.example.conf', './nginx.conf', domain='probe.42smart.com')

gen_conf('./supervisord.example.conf', './supervisord.conf', domain='probe.42smart.com')
