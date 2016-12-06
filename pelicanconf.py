#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

## Pelicon Config to be used in Development

AUTHOR = u'avi'
SITENAME = u'blag'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Feeds 
FEEDS =  (('All posts', 'feeds/all.atom.xml'),
          ('Category', 'feeds/category'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/iavins'),
          ('github', 'http://github.com/avinassh'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

## My Config mods start from here 
DEFAULT_CATEGORY = 'code'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
THEME = "skyfall"
GITHUB_URL = 'http://github.com/avinassh/'

DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['images', 'js', 'css', 'downloads']

ARTICLE_URL = '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}/index.html'

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

# For isso
# Specify where your isso server is running
ISSO_SERVER = '//localhost:8080/'
# Specify where is embed.js file, usually, it's your
# isso-server/js/embed.min.js
ISSO_EMBED_JS = '//posativ.org/isso/api/js/embed.min.js'