from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    # the name will be searched through base.html and put the value (ls.name)
    # we can also loop throught the dict obj variable from our databasse and then pass into the render function

    # don't use the base.html as one of the view; just extend that
    # return render(response, "main/base.html", {"name": ls.name})
    return render(response, "main/todolist.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html")