# Title of the website (use in <title> and <h1>
WEBSITE_TITLE = ""

# Default templates theme to use (templates are in templates dir
WEBSITE_THEME = "default"

# FQDN to reach the website (for example : http://www.domain.tld)
WEBSITE_BASE_URL = ""

# Some HTML headers
WEBSITE_AUTHOR = ""
WEBSITE_KEYWORDS = ""
WEBSITE_DESCRIPTION = ""

# FQDN to reach you media (photos, videos, ...)
WEBSITE_MEDIA_URL = WEBSITE_BASE_URL + '/media'

# Default order to use for listing posts on the home page
# The value is in the form of : <pattern>-<order>
POSTS_SORT = "date-DESC"

# Default parser (only mdown and plain are allowed)
PARSER = 'mdown'

# Activate RSS feed
RSS = True

# Subdirectory which contains raw posts
DATA_DIR = "data"

# Output subdirectory after generating the website
OUT_DIR = "out"
