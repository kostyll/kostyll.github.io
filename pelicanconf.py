#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Andrew V.'
SITENAME = u'LifeDebuger stuff'
SITEURL = '/'

PATH = 'content'
PLUGIN_PATHS = ['plugins/third_party/pelican-plugins/']
PLUGINS = ['assets', 'code_include','interlinks','pdf', 'sitemap','disqus_static']

#THEME='themes/third_party/pelican-themes/pelican-bootstrap3'
THEME='themes/third_party/pelican-fresh'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

GITHUB_URL = 'https://github.com/kostyll'

STATIC_COMMENTS = True
STATIC_COMMENTS_DIR = 'comments'

STATIC_PATHS = ['images',]

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

SITEMAP = {
'format': 'xml',
'priorities': {
'articles': 0.5,
'indexes': 0.5,
'pages': 0.5
},
'changefreqs': {
'articles': 'monthly',
'indexes': 'daily',
'pages': 'monthly'
}
}

disqus_secrets = map(lambda x: x.strip(),file('disqus_secrets').readlines())
print disqus_secrets

DISQUS_SITENAME = disqus_secrets[0].split(', ')[0]
DISQUS_SECRET_KEY = disqus_secrets[1]
DISQUS_PUBLIC_KEY = disqus_secrets[2]
