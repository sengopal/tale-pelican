AUTHOR = 'Senthil'
SITENAME = 'pelican-test'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

THEME = '../tale-pelican-theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

GOOGLE_ANALYTICS_ID = '' # Leave empty for now, or add your GA tracking ID
MENUITEMS = (
    ('Posts', '/'),
    ('Tags', '/tags.html'),
    ('About', '/pages/about.html'),
)
FOOTER_START_YEAR = 2021
FOOTER_END_YEAR = 2026 # Assuming current year for the example
FOOTER_INFO = 'Made with Pelican with Tale-Zola theme.'
KATEX_ENABLED = False
DISQUS_SITENAME = '' # Your Disqus shortname
DISQUS_DISCUSSION_TEXT = 'Discussion and feedback'
WRITTEN_BY_TEXT = 'Written by'
ON_TEXT = 'on'
P404_TITLE = '404: Page not found'
P404_INFO = 'Oops! We can\'t seem to find the page you are looking for.'
P404_BACK_HOME_TEXT_START = 'Let\'s'
P404_BACK_HOME_TEXT_LINK = 'head back home'
P404_BACK_HOME_TEXT_END = '.'


