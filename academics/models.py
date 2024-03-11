import datetime
from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    age = models.IntegerField()
    ident_number = models.CharField(max_length = 12, blank = True)
    create_at = models.DateTimeField(default = datetime.datetime.now())
    update_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)