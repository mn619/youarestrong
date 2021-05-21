from django.http.request import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.models import comments, blog_post, events, user_events

# Create your views here.

def post_comment(request):
    comment = comments()

    comment.blog = blog_post.objects.get(pk=request.POST['blog_id'])
    comment.aurthor = request.user
    comment.text = request.POST['text']

    comment.save()

    return redirect('app:blog-detail', blog_id=request.POST['blog_id'])

def post_blog(request):
    blog = blog_post()

    blog.title = request.POST['title']
    blog.content = request.POST['content']
    blog.aurthor = request.user
    blog.save()

    return redirect('app:home')

def create_event(request):
    print(request.POST)


    event = events()
    event.name = request.POST['name']
    event.speaker = request.user
    event.place = request.POST['place']

    event.save()

    return redirect('app:events-page')

def register_for_event(request):
    event = events.objects.get(pk=request.POST['event_id'])

    if user_events.objects.filter(user=request.user, event=event).exists() == False:
        user_event = user_events()
        user_event.user = request.user
        user_event.event = event
        user_event.save()
    
    return HttpResponse("200")

def deregister_for_event(request):
    event = events.objects.get(pk=request.POST['event_id'])

    if user_events.objects.filter(user=request.user, event=event).exists() == True:
        user_event = user_events.objects.get(user=request.user, event=event)
        user_event.delete()
    
    return HttpResponse("200")