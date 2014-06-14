from markdown import markdown
from pymongo import MongoClient
from bson import json_util
from collections import Counter
import datetime

from django.shortcuts import render
from django.http import HttpResponse
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

    return render(request, 'blog/blog_index.html',
                  {
                      'posts': posts,
                      'active_category': cat_name,
                      'archive': get_archive(),
                      'categories': get_categories(),
                  })


def about(request):
    """
    about page
    """
    return render(request, 'blog/about_me.html',
                 {
                     'active_category': 'about',
                     'categories': get_categories(),
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
                      'categories': get_categories(),
                  })


def archive(request, published_on):

    posts = Post.objects.filter(
        date__year=published_on[:4],
        date__month=published_on[5:7]).values('id', 'title')
    return render(request, 'blog/archive_list.html',
                  {
                      'date': published_on,
                      'archive': get_archive(),
                      'posts': posts,
                      'categories': get_categories(),
                  })


def mark_down(posts):
    for post in posts:
        post.body = markdown(post.body)
    return posts


def paginate(posts, page_num=1):
    paginator = Paginator(posts, 3)
    try:
        page = int(page_num)
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return posts


def json_gate_way(request, json_type):
    if request.method == 'GET':
        if json_type.lower() == 'category':
            return HttpResponse(json_util.dumps(Category.objects.values('name', 'description')))
        elif json_type.lower() == 'recent':
            return HttpResponse(json_util.dumps(Post.objects.values('id', 'title').order_by('-date')[:10]))
        elif json_type.lower() == 'comment':
            comment_list = get_comments()
            return HttpResponse(json_util.dumps(comment_list))


def comment(request):
    if request.method == 'POST':
        mail = request.POST.get('your_mail', '')
        your_comment = request.POST.get('your_comment', '')
        if your_comment == '':
            return HttpResponse("You failed!")
        insert_comment(mail, your_comment)
        return HttpResponse("Thank you!")


def get_comments():
    client = MongoClient('localhost', 27017)
    db = client.catyblog
    collection = db.comments
    return collection.find()


def insert_comment(mail, cmt):
    if len(mail) == 0:
        mail = "anonymous"

    item = {'mail': mail, 'comment': cmt}
    MongoClient('localhost', 27017).catyblog.comments.insert(item)





def search(request, keyword):
    search_result = Post.objects.filter(body__search=keyword)
    return render(request, 'blog/search_result.html', {'result': search_result});


def get_archive():
    result = Counter(map(lambda date: datetime.datetime.strftime(date['date'], '%Y-%m'),
                         Post.objects.values('date')))
    return sorted(result.iteritems(), reverse=True)


def get_categories():
    categories = Category.objects.values('name', 'description')
    return categories