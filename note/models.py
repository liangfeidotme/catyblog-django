# -*- coding: utf-8 -*-

from django.db import models


class ToDoList(models.Model):
    todo_item = models.CharField(max_length=200)
    is_finished = models.BooleanField()

    def __unicode__(self):
        return ''.join([u'[已完成]' if self.is_finished else '']) + self.todo_item
