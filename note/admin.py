from django.contrib import admin
from note.models import ToDoList
# Register your models here.


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['is_finished', 'todo_item']
    list_editable = ['todo_item']

admin.site.register(ToDoList, ToDoListAdmin)