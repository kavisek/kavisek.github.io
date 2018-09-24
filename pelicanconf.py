#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kavi Sekhon'
SITENAME = 'Kavi Sekhon'
SITEURL = 'https://kavisek.github.io'  # SITEURL = 'https://kavisek.github.io'

PATH = 'content'
THEME = '/Users/Kavi/Documents/Blog/theme/html5-dopetrope'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'https://github.com/kavisek'),
         ('Kaggle', 'https://www.kaggle.com/kavisek/'),
         ('StackExchange',
          'https://stackexchange.com/users/12639256/kavi-sek'),)


# Social widget
SOCIAL = (('http://twitter.com/kavisekh', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

STATIC_PATHS = ['images', 'extra/CNAME', 'pdfs', 'pages']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }


# --------- Additional Pelican Configurations --------

CACHE_CONTENT = False
CONTENT_CACHING_LAYER = 'reader'
CACHE_PATH = 'cache'
GZIP_CACHE = False
CHECK_MODIFIED_METHOD = 'mtime'
LOAD_CONTENT_CACHE = False
WITH_FUTURE_DATES = False
DEFAULT_DATE_FORMAT = '%d %b %Y'
GOOGLE_ANALYTICS = 'UA-126270550-1'

# --------- Additional HMTL5 Configurations --------

ABOUT_LINK = 'https://ca.linkedin.com/in/kavisek'  # What this all about? Section
ABOUT_IMAGE = 'images/kavi.png'  # Image to show at the bottom right of the page.
ABOUT_TEXT = """ Recently relocated to Toronto Ontario, currently seeking
employment at firm that uses Data Science for good. All the notebooks for each
article can be found on my github account under the "Data Science" repo
(https://github.com/kavisek/DataScience).

"""
ADDRESS = 'Toronto, Ontario'
MAIL = 'kavi.skhon@gmail.com'
# PHONE : Your phone number.
TWITTER_USER = 'kavisekh'  # 'Pierre_Paul', should be the url following http://twitter.com/
# GOOGLEPLUS_USER : '110831175850960549188', should be the url following http://plus.google.com/ when viewing your profile.
# Again, should be the URL following http://linkedin.com/ when viewing your profile.
LINKEDIN_USER = 'in/kavisek'
# FACEBOOK_USER : 'pierrepaul.lefebvre', if set in your profile, your profile can be accessed with a simple url like : https://facebook.com/pierrepaul.lefebvre

# Any text set here will show up on the bottom right of the page.
# If SHOW_COPYRIGHT is not set to False, it will show the copyright for html5up, credits for the images and the name set in this variable. You may want to set this variable to your name.
COPYRIGHT = 'Kavi Sekhon'
SHOW_COPYRIGHT = False  # True by default, you can set it to False to hide the copyrights.

DEFAULT_DATE = '2018-8-01 00:00'
DEFAULT_CATEGORY = 'Novice'
