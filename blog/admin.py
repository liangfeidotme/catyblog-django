from django.contrib import admin
from blog.models import Post, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):

    # def upper_case_name(self, obj):
    #     return ("%s %s" % (obj.title, obj.category)).upper()
    # upper_case_name.short_description = 'Name'

    search_fields = ['title']
    list_display = ['title', 'type', 'created_on']
    list_display_links = ['title', 'type', 'created_on']
    # list_editable = ['title']
    list_filter = ('category__description', 'date')
    # list_display = ('upper_case_name',)
    date_hierarchy = 'date'

    radio_fields = {'category': admin.HORIZONTAL}
    # raw_id_fields = ('category',)
    # change page
    fieldsets = (
        ('Article', {
            'description': '<em style="color:red;">Write your article here!</em>',
            'fields': ('category', 'title', 'body'),
            'classes': ('wide', )
        }),
        ('Comments', {
            'classes': ('collapse',),
            'fields': ()
        })
    )

    # readonly_fields = ('title',)
    # fields = ('title', 'category', 'body')

admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Category, CategoryAdmin)
