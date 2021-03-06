Installation
============

PyCMS need python >= 3.3 to works. Jinja2 template library is also required :

```
# pip install jinja2
```

If you want to use markdown in your blog post, you need to install the mardown extension for python :

```
# pip install markdown2
```

If you want to use the syntax highlighting in your code, install pygments :

```
# pip install pygments
```

If you want to generate a RSS feed :

```
# pip install PyRSS2Gen
```

Now, clone the pycms source repository into a location of your webserver directory tree :

```
$ git clone <repository_url>
```

Next, make a copy of the settings file and configure it :

```
$ cp settings.sample.py settings.py
$ vi settings.py
```

**settings.py** file has a lot of comments so you can edit it easily.

If you want to use markdown in most of your posts, the best solution is to set **PARSER** to **mdown** in the settings.py file.
