from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse(":::Welcom to my site:::")

def list_person(request):
    return HttpResponse ("Here you find a list of people")