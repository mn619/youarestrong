from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path(r'post_comment/', views.post_comment, name="post_comment"),
    path(r'post_blog', views.post_blog, name="post_blog"),
    path(r'create-event', views.create_event, name="create-event"),
    path(r'register-for-event', views.register_for_event, name="register-for-event"),
    path(r'deregister-for-event', views.deregister_for_event, name="deregister-for-event"),
]
