#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sirkia<br>Kelner<br>Knox'
SITENAME = u'Rocket Blog'
# SITEURL = 'http://blog.rocketlistings.com'
USER_LOGO_URL = "theme/images/logo.png"
TAGLINE = "The joint blog of three<br>Rocket Engineers."

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Launchrock Page', 'http://signup.rocketlistings.com/'),)

# Social widget
SOCIAL = () #('Another social link', '#'),)

MARKUP = ('rst', 'md', 'html')

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/rocket'

PLUGIN_PATH = "plugins"
PLUGINS = ['assets']
WEBASSETS = True
INTERNET_DEFENSE_LEAGUE = True