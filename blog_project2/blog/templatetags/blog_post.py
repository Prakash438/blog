from blog.models import *
from django import template
from django.db.models import Count
register = template.Library()

@register.simple_tag
def total_post():
    return Post.objects.count()

@register.inclusion_tag('blog/latest_post.html')
def show_latest_post(count=3):
    latest_post =Post.objects.order_by('-publish')[:count]
    return {'latest_post':latest_post}

@register.inclusion_tag('blog/most_commented_post.html')
def get_most_commented_posts(count=5):
    most_commented_post =  Post.objects.annotate(total_comment = Count('comments')).order_by('-total_comment')[:count]
    return {'ms':most_commented_post}