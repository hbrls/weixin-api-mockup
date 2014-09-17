# -*- coding: utf-8 -*-


def text(di, id, name_index=1):
    if id in di:
        return di[id][name_index]
    else:
        return u'未知'


def assemble_choices(di, id_index=0, name_index=1):
    return [(v[id_index], v[name_index]) for k, v in di.items()]


def validate(di, form_data, id_index=0, name_index=1):
    return form_data in [v[id_index] for k, v in di.items()]
