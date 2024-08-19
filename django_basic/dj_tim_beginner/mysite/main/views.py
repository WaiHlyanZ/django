from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>Index page</h1>")

def main(response):
    return HttpResponse("<h1>Main page</h1>")

def view1(response):
    return HttpResponse("<h1>View 1 page</h1>")