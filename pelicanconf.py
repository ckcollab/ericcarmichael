#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os


AUTHOR = 'Eric Carmichael'
SITENAME = "Eric Carmichael's Nerdery"
SITEURL = os.environ.get("PELICAN_SITE_URL", "")

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 2
# WITH_FUTURE_DATES = True

GITHUB_URL = 'http://github.com/ckcollab/'
THEME = "themes/mintheme"
PATH = "content"
PLUGINS = ["plugins.assets", "plugins.sitemap"]
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
        "articles": "daily",
        "pages": "daily",
        "indexes": "daily",
    }
}

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Make pages/*.html not require 'title' attribute thing
READERS = {'html': None}

# Make the site display full articles instead of summaries by setting this to 0
# SUMMARY_MAX_LENGTH = 0
