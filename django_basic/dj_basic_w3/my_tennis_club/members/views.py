from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


# Create your views here.
def home(request):
    return render(request, "home.html")

def members(request):
    my_members = Member.objects.all().values()
    template = loader.get_template("my_first.html") # because of this line we see 
    context = {
        "my_members": my_members,
    }
    return HttpResponse(template.render(context, request))


