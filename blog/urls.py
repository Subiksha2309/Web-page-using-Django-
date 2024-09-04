from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<str:post_id>", views.detail, name="detail"),
    path("old_url", views.old_url, name="old_url"),
    path("new_url_some", views.new_url, name="new_url_page"),
]
