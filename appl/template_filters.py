# -*- coding: utf-8 -*-
from appl.dictionary import text
from appl.dictionary.location import LOCATIONS
from appl.dictionary.gender import GENDERS


def configure_template_filters(app):

    @app.template_filter('gravatar_default')
    def gravatar_default(gravatar):
        return 'http://www.gravatar.com/avatar/%s?s=160' % gravatar

    @app.template_filter('gravatar_small')
    def gravatar_small(gravatar):
        return 'http://www.gravatar.com/avatar/%s?s=32' % gravatar

    # Dictionaries
    @app.template_filter('d_gender')
    def d_gender(id):
        return text(GENDERS, id)

    @app.template_filter('d_location')
    def d_location(id):
        return text(LOCATIONS, id)
