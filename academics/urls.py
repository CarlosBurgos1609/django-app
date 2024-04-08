from django.urls import path

from . import views
urlpattenns = [
    path("", views.index, name='index')
]