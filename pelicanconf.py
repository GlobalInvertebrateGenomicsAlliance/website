#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'GIGA'
SITENAME = 'GIGA - Global Invertebrate Genomics Alliance'
SITEDESCRIPTION = 'Website for the Global Invertebrate Genomics Alliance'
SITEURL = 'https://GlobalInvertebrateGenomicsAlliance.github.io/website'

# plugins
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['i18n_subsites', 'tipue_search']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = 'theme'
I18N_GETTEXT_LOCALEDIR = 'theme/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# content paths
PATH = 'content'
PAGE_PATHS = ['pages/en']
ARTICLE_PATHS = ['blog/en']

# i18n
I18N_SUBSITES = {
  'de': {
    'PAGE_PATHS': ['pages/de'],
    'ARTICLE_PATHS': ['blog/de'],
    'LOCALE': 'de_DE'
  }
}

# logo path, needs to be stored in PATH Setting
LOGO = 'images/giga_logo.jpg'

# special content
HERO = [
  {
    'image': 'images/hero/background-1.jpg',
    # for multilanguage support, create a simple dict
    'title': {
      'en':'Some special content',
      'de': 'Spezieller Inhalt'
    },
    'text': {
      'en': 'Any special content you want to tease here',
      'de': 'Jeglicher spezieller Inhalt den Sie hier bewerben möchten'
    },
    'links': [
      {
        'icon': 'icon-code',
        'url': 'https://github.com/claudio-walser/pelican-fh5co-marble',
        'text': 'Github'
      }
    ]
  }, {
    'image': 'images/hero/background-2.jpg',
    # keep it a string if you dont need multiple languages
    'title': 'Uh, special too',
    # keep it a string if you dont need multiple languages
    'text': 'Keep hero.text and hero.title a string if you dont need multilanguage.',
    'links': []
  }, {
    'image': 'images/hero/background-3.jpg',
    'title': 'No Blogroll yet',
    'text': 'Because of space issues in the man-nav, i didnt implemented Blogroll links yet.',
    'links': []
  }, {
    'image': 'images/hero/background-4.jpg',
    'title': 'Ads missing as well',
    'text': 'And since i hate any ads, this is not implemented as well',
    'links': []
  }
]

# Social widget
SOCIAL = (
  ('Github', 'https://github.com/GlobalInvertebrateGenomicsAlliance'),
  ('Facebook', 'https://www.facebook.com/groups/1554768864811769/'),
  ('Twitter', 'https://twitter.com/GIGA_COS?lang=en'),
  ('slack', 'https://giga-cos.slack.com/')
)

ABOUT = {
  'image': 'images/about/about.jpeg',
  'mail': 'info@gitcd.io',
  # keep it a string if you dont need multiple languages
  'text': {
    'en': 'Learn more about the creator of this theme or just drop a message.',
    'de': 'Lernen Sie den Author kennen oder hinterlassen Sie einfach eine Nachricht'
  },
  'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'Nova Southeastern University',
  'phone': '954-242-3600'
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'

MENUITEMS = [
  ('Archive', 'archives.html'),
  ('Contact', 'contact.html')
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'search', # needed for tipue_search plugin
  'contact' # needed for the contact form
]

# setup disqus
DISQUS_SHORTNAME = 'giga-1'
DISQUS_ON_PAGES = False # if true its just displayed on every static page, like this you can still enable it per page

# setup google maps
#GOOGLE_MAPS_KEY = 'AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA'
