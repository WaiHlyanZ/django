# Basic Django working flow

views.py to render the objects
urls.py to map each object inside views.py

we need to link sub-app urls.py to main-app mysite's urls.py (same name as the project)

Let say
our `mysite/urls.py`'s:


```
urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include("main.urls")),
]
```

the user'path is `http://127.0.0.1:8000/home/start`

we will look is anything match to home/ in `mysite/urls.py` 

it was so it go `main.urls` and search for is  `start` in `main.urls.urlpatterns` then it is do the specifice function
