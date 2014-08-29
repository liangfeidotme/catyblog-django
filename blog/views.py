from markdown import markdown
from collections import Counter
import datetime

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
                  {
                      'posts': posts,
                      'active_category': cat_name,
                      'archive': get_archive(),
                      'categories': article_count_per_category(),
                      'nav_name': 'blog',
                  })


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
                  {
                      'post': post,
                      'active_category': post.category.name,
                      'archive': get_archive(),
                      'categories': article_count_per_category(),
                      'nav_name': 'blog',
                  })


def archive(request, published_on):

    posts = Post.objects.filter(
        date__year=published_on[:4],
        date__month=published_on[5:7]).values('id', 'title')
    return render(request, 'blog/archive.html',
                  {
                      'date': published_on,
                      'archive': get_archive(),
                      'posts': posts,
                      'categories': article_count_per_category(),
                      'nav_name': 'blog',
                  })


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
