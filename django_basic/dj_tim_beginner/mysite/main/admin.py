from django.contrib import admin
from .models import ToDoList, Item
# Register your models here.
# Username = waihlyan
# password = Zadmin@90807060504030

# register to see on the admin website
admin.site.register(ToDoList)
admin.site.register(Item)