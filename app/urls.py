from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path(r'', views.home_view, name="home"),
    path(r'blog/<int:blog_id>/',views.blog_detail, name="blog-detail"),
    path(r'events', views.events_page, name="events-page"),
    path(r'my-events', views.my_events_page, name="my-events-page"),
]