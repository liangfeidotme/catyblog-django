from django.http import HttpResponse
from markdown import markdown
from collections import Counter
import datetime
import json

from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from blog.models import Post, Category

"""""""""""""""""""""""""""
view functions
"""""""""""""""""""""""""""


def index(request, cat_name, page_num=1):
    """
    Home page
    """
    if cat_name.lower() == 'home':
        posts = Post.objects.all().order_by('-date')
    else:
        posts = Post.objects.all().filter(category__name=cat_name).order_by('-date')

    posts = paginate(mark_down(posts), page_num)

    # return HttpResponse(article_count_per_category())

    return render(request, 'blog/index.html',
                  fill_page_with(posts=posts, nav_name='blog', active_category=cat_name))


def article(request, article_id):
    """
    article details page
    """
    posts = Post.objects.filter(id=int(article_id))
    if posts.count() == 0:
        return render(request, 'blog/article.html')

    post = posts[0]
    post.body = markdown(post.body)

    return render(request, 'blog/article.html',
                  fill_page_with(post=post, active_category=post.category.name, nav_name='blog'))


def archive(request, published_on):

    posts = Post.objects.filter(
        date__year=published_on[:4],
        date__month=published_on[5:7]).values('id', 'title')
    return render(request, 'blog/archive.html',
                  fill_page_with(date=published_on, posts=posts, nav_name='blog'))


def tag(request, tag_name):
    return render(request, 'blog/tag_filter.html',
                  fill_page_with(articles=search_by_tag(tag_name), tag=tag_name, nav_name='blog'))


def fill_page_with(**kwargs):
    base_dict = \
        {
            'archive': get_archive(),
            'categories': article_count_per_category(),
            'tags': get_tags(),
            'recent_published': get_recently_published(5),
        }
    base_dict.update(kwargs)
    return base_dict


def mark_down(posts):
    for post in posts:
        post.body = markdown(post.body)
    return posts


def paginate(posts, page_num=1):
    paginator = Paginator(posts, 2)
    try:
        page = int(page_num)
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return posts


def get_archive():
    result = Counter(map(lambda date: datetime.datetime.strftime(date['date'], '%Y-%m'),
                         Post.objects.values('date')))
    return sorted(result.iteritems(), reverse=True)


def get_categories():
    categories = Category.objects.values('name', 'description')
    return categories


def article_count_per_category():
    return Counter(post.category for post in Post.objects.all()).iteritems()


def get_tags():
    tags = set()
    for post in Post.objects.all():
        for tag in post.tags.all():
            tags.add(tag.name)
    return tags


def search_by_tag(tag_name):
    articles = set()
    for post in Post.objects.all():
        if tag_name in (tag.name for tag in post.tags.all()):
            articles.add((post.id, post.title))
    return articles


def get_recently_published(num):
    assert num > 0
    posts = Post.objects.order_by('-date')
    if num < len(posts):
        posts = posts[:num]
    return [(post.id, post.title) for post in posts]
