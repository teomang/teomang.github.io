#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Orkung'
SITENAME = u'Anlatabildiklerim'
SITEURL = 'https://gunluk.orkungunay.com'

PATH = 'content'

TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
#AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
STATIC_PATHS = ['images', 'extra/CNAME', 'pdfs']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
THEME = "/Users/orkungunay/orkun/repos/diger/nikhil-theme"
PLUGIN_PATHS = ['/Users/orkungunay/orkun/repos/diger/pelican-plugins']
PLUGINS = [
    'sitemap',
    'feed_summary'
#   'disqus_static'
]
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
DISQUS_SITENAME = 'orkungunay'
DISQUS_SECRET_KEY = 'gEpV4X6QFbJrPisSAAt7aN1OWqCLntciqKsmtOMpCE78HtE4P40BXcRZKLGSWqXy'
# DISQUS_PUBLIC_KEY = u'YOUR_PUBLIC_KEY'
