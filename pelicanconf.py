#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

#from jinja2 import Environment as Jinja2Environment
#from webassets import Environment as AssetsEnvironment
#from webassets.ext.jinja2 import AssetsExtension

AUTHOR = u'Eric Carmichael'
SITENAME = u"Eric Carmichael's Nerdery"
SITEURL = os.environ.get("PELICAN_SITE_URL", "")

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 2

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

GITHUB_URL = 'http://github.com/ckcollab/'
THEME = "themes/mintheme"
PATH = "content"
PLUGINS = ["plugins.assets"]
WEBASSETS = True
'''
assets_env = AssetsEnvironment('./static/media', '/media')
jinja2_env = Jinja2Environment(extensions=[AssetsExtension])
jinja2_env.assets_environment = assets_env

JINJA_EXTENSIONS = []
JINJA_EXTENSIONS.append(AssetsExtension)
print JINJA_EXTENSIONS
'''
