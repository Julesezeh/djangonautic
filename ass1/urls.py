from django.urls import path
from ass1 import views

urlpatterns = [
    path("",views.signup,name='signup'),
    path("<str:slug>/",views.customers),
]