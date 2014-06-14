from django.contrib import admin
from blog.models import Post, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'category', 'date']
    date_hierarchy = 'date'

    # change page
    fieldsets = (
        ('Article', {
            'description': 'Write your article here!',
            'fields': ('category', 'title', 'body'),
            'classes': ('wide', )
        }),
        ('Comments', {
            'classes': ('collapse',),
            'fields': ()
        })
    )

    #fields = ('title', 'category', 'body')

admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Category, CategoryAdmin)
