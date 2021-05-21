from django.contrib import admin
from .models import blog_post, comments, events, user_events
# Register your models here.

admin.site.register(blog_post)
admin.site.register(comments)
admin.site.register(events)
admin.site.register(user_events)
