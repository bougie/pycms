PYCMS
=====

PyCMS is a small cms used to generate a static website like a blog.

## Installation

PyCMS need jinja2 template library :

```
# pip install jinja2
```

And that's all ! Simply clone the pycms source repository into a location of your webserver directory tree. Next :

```
$ cp settings.sample.py settings.py
$ vi settings.py
```

### Plugins

If you want to use markdown in your post files, you need to install the mardown extension for python :

```
# pip install mardown
```

Then, if you want to use markdown in the most of your posts, the best solution is to set **PARSER** to **mdown** in the settings.py file.

## How-to

PyCMS is pretty simple to using it.
Write some blog post in the DATA_DIR. Filename have to have .md extension.
After writing posts, lauch this command :

```
$ python parse.py
```

This script will generate all html static file from your *.md posts.

### Blog .md file content

```
title: title of the post
parser: mdown / plain / html

the content of the post
```

**The blank line is not a typo. This line is mandatory !**
The header line **parser** is not required if you set PARSER configuration variable. But you con use a different parser for only one post, and in this case, you have to set this header.

### Blog links menu

You can add a menu with static links. All will be in the **<data_dir>/links.txt** file.
The syntax is similary to blog post :

```
parser: mdown / plain / whatever

link1
link2
linkN
```

Like blog post, the header line **parser** is not required.
