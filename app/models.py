from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blog_post(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=1024)
    aurthor = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

class comments(models.Model):
    blog = models.ForeignKey(blog_post, on_delete=models.CASCADE)
    aurthor = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1024)
    
class events(models.Model):
    name = models.CharField(max_length=64)
    time = models.DateTimeField(auto_now_add=True)
    speaker = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    place = models.CharField(max_length=128)

class user_events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(events, on_delete=models.CASCADE)

