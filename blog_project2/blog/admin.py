from django.contrib import admin
from blog.models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','status',]
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status','author','created','publish')
    search_fields = ('title','body')
    date_hierachy = 'publish'
    raw_id_fields = ('author',)
    ordering =['status','publish']
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)