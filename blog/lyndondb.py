__author__ = 'lyndon'

from pymongo import MongoClient
from blog.models import Post


class CatyBlogDB:
    def __init__(self):
        with MongoClient('localhost', 27017) as mc:
            self.articles = mc.catyblog.articles

    def insert(self, article):
        self.articles.insert({'title': article.title, 'body': article.body})

    def backup_mysql(self):
        posts = Post.objects.all()
        for post in posts:
            self.insert(Article(post.title, post.body))


class Article:
    def __init__(self, title, body):
        self.title = title
        self.body = body
