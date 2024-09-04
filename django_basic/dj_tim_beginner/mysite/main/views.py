from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    tasks = ls.item_set.get(id=1)
    # return HttpResponse(f"<h1>{ls.name}</h1>\n<h2>{tasks}</h2>")
    return HttpResponse("<h1>%s</h1><br><p>%s</p>" %(ls.name, tasks.text))

def home(response):
    return HttpResponse("<h1>Home page</h1>")