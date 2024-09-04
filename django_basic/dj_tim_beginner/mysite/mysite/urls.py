"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #ip_address/home ဆိုရင် main.urls ထဲက root path ကိုလိုက်ရှာမယ် `path("", views.index, name="index"),` views ထဲ က index function ကို အလုပ်လုပ်မယ်
    #ip_address/home/v1 ဆိုရင် main.urls ထဲက root path ကိုလိုက်ရှာမယ် `path("/v1", views.view1, name="view_1"),` views ထဲ က view1 function ကို အလုပ်လုပ်မယ် 
    #                                                                    /v1 ဆိုတဲ့ရေးပုံလေးက sub-url ဆိုတဲ့သဘော
    path("", include("main.urls")), 

]
