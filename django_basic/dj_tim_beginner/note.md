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

### Navigating urls and views

sub-app.urls ကို သွားစေချင်ရင် project နဲ့ နာမည်အတူတူ main-app ထဲက urls.py ထဲမှာ ကိုယ်သွားစေချင်တဲ့ url name ထားပါတော့ home/ ဆိုရင် home နဲ့ဆိုင်တဲ့ app.urls ထဲသွားပေါ့ ပြီးမှ home/ ရဲ့ နောက်က ဘာဆက်ပါလဲ home/v1 ဆိုရင် home/ ဒါမှမဟုတ် home ကြီးက အစောပိုင်း main-app.urls ထဲမှာ တူလို့ဖြတ်ယူပြီးသွားပြီ ကျန်တာက /v1 ဒါမှမဟုတ် v1 u sub-app.urls ထဲမှာ ရှိတယ်ဆိုရင် သူ run စေချင်တဲ့ function ကို run ပေါ့

### Database in Django

create models (classes) in models.py

write your fields in that classes

instance variable of model.Field are the name of that field

then tell Django that you setup the db by putting `app_name.apps.PollsConfig` inside `INSTALLED_APPS`

in this case `main.apps.MainConfig` is added inside `INSTALLED_APPS`

After all,

```
# run this
pythonmanage.pymakemigrationspolls
```

Then you will see like this:

```
D:\Data\main\self\v2_door\programming\web_dev\django\django_basic\dj_tim_beginner\mysite>python -m manage makemigrations main
Migrations for 'main':
  main\migrations\0001_initial.py
    - Create model ToDoList
    - Create model Item
```

To apply changes:

```
python manage.py migrate
```

* Change your models (in models.py).
* Run python manage.py makemigrations to create migrations for those changes
* Run python manage.py migrate to apply those changes to the database.
