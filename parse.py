import sys
import os
import logging

try:
    import settings
except:
    print("No config file found")
    sys.exit(1)

logging.basicConfig(
    format='%(asctime)s PYCMS %(levelname)s %(message)s',
    level=logging.DEBUG
)

from lib.post import PostsManager
from lib.function import save_tpl
from lib.static import move_files
from lib.link import Link
from lib.tag import TagManager
from lib.rss import RSS

from jinja2 import Environment, FileSystemLoader


def main():
    if len(settings.DATA_DIR) == 0 or len(settings.OUT_DIR) == 0:
        logging.error("MAIN Please fill correctly the config file")
        sys.exit(1)

    if not os.path.isdir(settings.DATA_DIR):
        logging.error("MAIN Data dir '%s' does not exist" % (settings.DATA_DIR))
        sys.exit(1)

    if not os.path.isdir('template/%s' % (settings.WEBSITE_THEME)):
        logging.error(
            "MAIN Theme '%s' does not exist" % (settings.WEBSITE_THEME))
        sys.exit(1)

    if not os.path.isdir(settings.OUT_DIR):
        try:
            os.mkdir(settings.OUT_DIR)
        except Exception as e:
            logging.error(str(e))
            sys.exit(1)

    posts = PostsManager()

    posts.generate_list(path=settings.DATA_DIR)
    if len(posts.posts_list) == 0:
        logging.error("MAIN Please write some posts before doing a parse")
        sys.exit(1)

    theme_dir = 'template/%s' % (settings.WEBSITE_THEME)

    tplenv = Environment()
    tplenv.loader = FileSystemLoader(theme_dir)

    #
    # Generate links
    #
    links = Link()
    links.parse()

    common_args = {
        'base_url': settings.WEBSITE_BASE_URL,
        'page_title': settings.WEBSITE_TITLE,
        'page_author': settings.WEBSITE_AUTHOR,
        'page_keywords': settings.WEBSITE_KEYWORDS,
        'page_description': settings.WEBSITE_DESCRIPTION,
        'links': links.get(),
        'tags': '',
        'media_url': 'media'
    }

    #
    # Posts generation
    #
    index_posts_list = posts.parse()

    #
    # Sort posts list on the home page
    #
    sort = 'date'  # sort by date by default
    sort_revers_order = True  # sort in revers order by default
    usersort = settings.POSTS_SORT.split('-')
    if len(usersort) == 2:
        if usersort[0] in ['date', 'title']:  # Allowed sort filter
            sort = usersort[0]
            if usersort[1] == 'ASC':
                sort_revers_order = False
            elif usersort == 'DESC':
                sort_revers_order = True

    index_posts_list = sorted(
        index_posts_list,
        key=lambda pst: pst[sort],
        reverse=sort_revers_order
    )

    # RSS generator
    #
    # Base class for generating RSS feed
    if settings.RSS:
        rss = RSS(
            link='%s/feed' % (settings.WEBSITE_BASE_URL),
            title='%s feed' % (settings.WEBSITE_TITLE),
            description='%s' % (settings.WEBSITE_TITLE)
        )
        # Sort post list by date if not did
        if sort != 'date' or sort_revers_order is not True:
            rss_posts_list = sorted(
                index_posts_list,
                key=lambda pst: pst['date'],
                reverse=True
            )
        else:
            rss_posts_list = index_posts_list
        for p in rss_posts_list:
            rss.add_item(
                link=p.get('url_title'),
                title=p.get('title'),
                description=p.get('content'),
                date=p.get('date')
            )
        rss.save(date=posts.get_last_post_date())
        common_args['rss'] = rss.get_link()
        if len(common_args['rss']) > 0:
            common_args['activate_rss'] = True
    else:
        common_args['activate_rss'] = False

    #
    # Tags Manager - Used to generate tags cloud
    #
    tagsmgr = TagManager()
    tagsmgr.parse(posts=index_posts_list)
    common_args['tags'] = tagsmgr.get_list()
    tagsmgr.save(tplenv=tplenv, extra_args=common_args)

    #
    # save posts files
    #
    posts.save(tplenv=tplenv, extra_args=common_args)

    #
    # generate and save the home page
    #
    _args = {
        'page_title': settings.WEBSITE_TITLE,
        'page_name': 'Accueil - liste des billets',
        'posts': index_posts_list
    }
    _args.update(common_args)
    save_tpl(
        tplenv=tplenv,
        args=_args,
        tplname='index.tpl',
        dst=os.path.join(settings.OUT_DIR, 'index.html')
    )

    #
    # Move static file (css, js, img, ...)
    # from the template dir to the output dir
    #
    move_files(
        input_dir=os.path.join(theme_dir, 'static'),
        output_dir=os.path.join(settings.OUT_DIR, 'static')
    )

    #
    # Move data files from the subdir in data dir to the output dir
    #
    move_files(
        input_dir=os.path.join(settings.DATA_DIR, 'media'),
        output_dir=os.path.join(settings.OUT_DIR, 'media')
    )

if __name__ == "__main__":
    main()
