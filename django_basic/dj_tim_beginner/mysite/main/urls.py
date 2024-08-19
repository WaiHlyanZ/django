from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("main/", views.main, name="main view"),
    path("v1/", views.view1, name="view_1"),
]