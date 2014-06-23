from django.db import models
from django.utils.html import format_html
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=60)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def created_on(self):
        return self.date.strftime('%Y-%m-%d')
    created_on.short_description = 'Created on'

    def article_category(self):
        return format_html('<span style="color: red;">{0}</span>', self.category)
    article_category.short_description = 'Category'
    article_category.allow_tags = True
    article_category.admin_order_field = 'category'

    type = property(article_category)