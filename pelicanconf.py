#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os


AUTHOR = u'Eric Carmichael'
SITENAME = u"Eric Carmichael's Nerdery"
SITEURL = os.environ.get("PELICAN_SITE_URL", "")

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 2

GITHUB_URL = 'http://github.com/ckcollab/'
THEME = "themes/mintheme"
PATH = "content"
PLUGINS = ["plugins.assets", "plugins.sitemap", "plugins.autolinker"]
MARKUP = (('rst', 'md', 'html'))
WEBASSETS = True

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 1,
        "pages": 1,
        "indexes": 0
    },
    "changefreqs": {
        "articles": "weekly",
        "pages": "monthly",
        "indexes": "weekly",
    }
}
