#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

## Pelicon Config to be used in Production

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://avi.im/blag'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag/%s.atom.xml'

OUTPUT_PATH = '/Users/avi/Documents/code/blag/avinassh.github.io/blag/'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

# For isso
# Specify where your isso server is running
ISSO_SERVER = '//isso-avinassh.rhcloud.com/'
# Specify where is embed.js file, usually, it's your
# isso-server/js/embed.min.js
ISSO_EMBED_JS = '//posativ.org/isso/api/js/embed.min.js'