from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("l", views.list_person, name='list')
    
]