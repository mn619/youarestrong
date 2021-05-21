from django.db.models.fields import BooleanField, CharField, IntegerField
from django.shortcuts import redirect, render
from .models import blog_post, events, user_events
# Create your views here.

def home_view(request):
    blogs = blog_post.objects.all().order_by("-pk")

    return render(request, 'app/home.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    if blog_post.objects.filter(pk=blog_id).exists() == False:
        return render(request, 'app/unavaliable.html', {'title': "Blog unavaliable", 'error_message': "Blog do not exist"})
    
    blog = blog_post.objects.get(pk=blog_id)
    comments = blog.comments_set.all()

    return render(request, 'app/blog-detail.html', {'blog' : blog, 'comments' : comments})

def events_page(request):
    states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana',
              'Himachal Pradesh', 'Jharkhand', 'Karnataka ', 'Kerala', 'Madhya Pradesh ', 'Maharashtra ', 'Manipur ',
              'Meghalaya ', 'Mizoram ', 'Nagaland ', 'Odisha ', 'Punjab ', 'Rajasthan ', 'Sikkim ', 'Tamil Nadu ', 
              'Telangana ', 'Tripura ', 'Uttar Pradesh ', 'Uttarakhand ', 'West Bengal']

    _events = events.objects.filter(confirmed=True).order_by("-pk")

    return render(request, 'app/events.html', {'events': _events, 'states': states, 'page': 'Events'})

def my_events_page(request):
    if request.user.is_authenticated == False:
        return render(request, 'app/unavaliable.html', {'title': 'Page Unavaliable', 'error_message': 'Login to view'})

    _events = events.objects.filter(confirmed=True).order_by("-pk")
    user_event = []

    for e in _events:
        if user_events.objects.filter(user=request.user, event=e).exists():
            user_event.append(e)

    return render(request, 'app/events.html', {'events': user_event, 'page': 'MyEvents'})