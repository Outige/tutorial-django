from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tieg", views.tieg, name="tieg"),
    path("html/welcome", views.welcome, name="welcome"),
    path("<str:name>", views.greet, name="greet"),
    path("html/<str:name>", views.html, name="html"),
]