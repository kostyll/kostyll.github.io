#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Andrew V.'
SITENAME = u'LifeDebuger stuff'
SITEURL = '/'

PATH = 'content'
PLUGIN_PATHS = ['/home/andrew/build/pelican-plugins']
PLUGINS = ['assets', 'static_comments','code_include','interlinks','pdf']

THEME='/home/andrew/build/pelican-themes/pelican-bootstrap3'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

GITHUB_URL = 'https://github.com/kostyll'

STATIC_COMMENTS = True
STATIC_COMMENTS_DIR = 'comments'

STATIC_PATHS = []

PDF_GENERATOR = False
PDF_STYLE_PATH = ''
PDF_STYLE = 'a4'

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

INTERLINKS = {
        'wikipedia_en': 'http://en.wikipedia.org/wiki/',
        'ddg': 'https://duckduckgo.com/?q=',
        'google': 'https://google.com/search?q='
    }

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (#('You can add links in your config file', '#'),
          #('Another social link', '#'),
          ('GH','https://github.com/kostyll'),
          ('FB','https://www.facebook.com/andrew.vasyltsiv')
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ROOT = os.path.dirname(os.path.abspath(__file__))
