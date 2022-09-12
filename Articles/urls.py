from unicodedata import name
from django.urls import path
from django.urls.conf import re_path
from . import views
from .views import edit_article

app_name = 'particular'
urlpatterns = [
    path('',views.artyy,name="articles"),
    path('create',views.create_article,name='create'),
    path("<slug:slug>/",views.article_detail,name="detail"),
    path("edit/<slug:slug>", edit_article.as_view() ,name='edit'),
    path("log", views.log_view,name='log'),
]
