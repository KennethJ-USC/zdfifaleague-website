#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITEURL='http://zdfifaleague.com'

AUTHOR = u'Kenneth Johnson ZD215'
SITENAME = u'ZD FIFA League'
SITETITLE='ZD FIFA League'
SITESUBTITLE='Spring 2019 Season'
PATH = u'/home/kennethj/projects/fifazd/content/'
DEFAULT_LANG = u'en'
TIMEZONE = u'America/New_York'
THEME = '/var/www/pelican-themes/Flex'

LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True

READERS = {"html": None}
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
	'extra/placeholder.html': {'path': 'extra/placeholder.html'}
}
ARTICLES_EXCLUDES = ['extra']

SITELOGO = 'images/thetataulogo.png'

FEED_ATOM = None
FEED_RSS = None

MAIN_MENU = True

MENUITEMS = (
	('League Spreadsheet', 'https://docs.google.com/spreadsheets/d/1X9XxHslgMVaPTzr7v3JsIexOWhY6Z2DmAk7ddO4r4cM/edit?usp=sharing'),
	('Contact', 'extra/placeholder.html'),)


LINKS = (('Standings', 'extra/placeholder.html'),
	('About', 'extra/placeholder.html'),
	('Rules', 'extra/placeholder.html'),)

USE_FOLDER_AS_CATEGORY = True
