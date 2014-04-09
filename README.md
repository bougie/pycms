PYCMS
=====

PyCMS is a small cms used to generate a static website like a blog.

## Installation

PyCMS need jinja2 template library :
```
# pip install jinja2
```

And that's all ! Simply clone the pycms source repository into a location of your webserver directory tree. Next:
```
# cp settings.sample.py settings.py
# vi settings.py
```

## How-to

PyCMS is pretty simple to using it.\\
Write some blog post in the DATA_DIR. Filename have to have .md extension.\\
After writing posts, lanch this command :
```
# python parse.py
```
This script will generate all html static file from your *.md posts.

### Blog .md file content
```
title: title of the post

the content of the post
```
The blank line is not a typo. This line is mandatory !
