from django.db import models

# In Django class is a table anyway
class Member(models.Model):
    """
    The table is not created yet! 
    To actually create the table in the database:

    Type `python manage.py makemigrations <app name>` in CMD to add 0001_initial.py, in my case app name is members
    Type `python manage.py migrate` in CMD to create a table in db.sqlite3

    Want to view SQL statement
    Type `python manage.py sqlmigrate members 0001` in CMD

    To add members
    Type `python manage.py shell` in CMD
    """
    # Table fields 
    first_name = models.CharField(max_length=255) # CharField is the same as text data type in access
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
