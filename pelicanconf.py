#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'danclaudiupop'
SITENAME = u'blog.danclaudiupop'
SITEURL = 'http://localhost:8000'
FEED_DOMAIN = SITEURL
TAGLINE = 'Software Testing and more'

TIMEZONE = 'Europe/Bucharest'
DEFAULT_DATE_FORMAT = ('%d %B %Y')

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extra/CNAME']

THEME = "theme/skeleton/"
GOOGLE_ANALYTICS = "UA-62968573-1"
DISQUS_SITENAME = "blog.danclaudiupop"

MENUITEMS = [('Posts', ''), ('About', 'about.html')]
SOCIAL = (
    ('rss', 'http://blog.danclaudiupop.com/feeds/all.atom.xml'),
    ('github', 'https://github.com/danclaudiupop/'),
    ('twitter', 'https://twitter.com/danclaudiupop'),
)
DISPLAY_PAGES_ON_MENU = False

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

PAGE_URL = PAGE_SAVE_AS = '{slug}.html'

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

RELATIVE_URLS = False
