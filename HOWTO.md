HOWTO
=====

PyCMS is pretty simple to using it.
Write some blog post in the DATA_DIR. Filenames have to use .bp extension.
After writing posts, lauch this command :

```
$ python parse.py
```

This script will generate all html files from your *.bp posts.

### Blog .bp file content

A blog post is make in two different part :
  * headers : contains post title, tags, ...
  * content : content of the body of the post

```
title: title of the post
parser: mdown / plain / whatever
tags: tag1,tag2, tag3

the content of the post
```

**The blank line is not a typo. This line is mandatory to separate headers part to content one !**

#### Headers

  * **parser** is not required if you set PARSER in settings.py file. But you con use a different parser for only one post, and in this case, you have to set this header. Only **mdown** and **plain** are supported.
  * **tags** is not required. Specify a list of words separated by a ','.

#### Content

You can write your text like you want according to the parser (or the default parser) selected in the settings.py.

### Blog links menu

You can add a menu with static links. All items will be in the **<DATA_DIR>/links.txt** file.
The syntax is similary to blog post :

```
parser: mdown / plain / whatever

link1
link2
linkN
```

Like blog post, the header line **parser** is not required.