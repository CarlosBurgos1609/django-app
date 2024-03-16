import datetime
from django.db import models

# Create your models here.
# model1.DateTimeField(auto_now = True, null = false)
class User(models.Model):
    email = models.EmailField(null = True, blank = False)    
    password = models.CharField(null = True, blank = False)
    status = models.BooleanField(default = True)
    create_at = models.DateTimeField(default = datetime.datetime.now())
    update_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)
    
class Person(models.Model):
    firstname = models.CharField(max_length = 20, blank = False)
    lastname = models.CharField(max_length = 20, blank = False)
    age = models.IntegerField(max_length = 15, blank = False)
    id_ident_type = models.ForeignKey('Identification_types', on_delete = models.CASCADE, blank = False)
    ident_number = models.CharField(max_length = 12, blank = False)
    id_exp_city = models.ForeignKey( 'Cities', on_delete = models.CASCADE, blank = False)
    address = models.CharField()#max_Length = 150)
    mobile = models.CharField( )#max_Length = 50, blank = False)
    id_user = models.ForeignKey( 'User', on_delete = models.CASCADE, blank = False)
    create_at = models.DateTimeField(default = datetime.datetime.now())
    update_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)
    
class Students(models.Model):
    code = models.CharField(max_length=50, blank = True)
    id_person = models.ForeignKey('Person', on_delete = models.CASCADE, blank = False)
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)
    
class Identification_types(models.Model):
    name = models.CharField(max_length = 50, blank = False)
    abrev = models.CharField(max_length = 10, blank = False)
    descript =  models.CharField(max_length = 100, blank = False)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)
    
class Cities(models.Model):
    name = models.CharField(max_length = 10, blank = False)
    abrev = models.CharField(max_length = 10, blank = False)
    descript =  models.CharField(max_length = 10, blank = False)
    id_dept = models.ForeignKey("Departaments", on_delete = models.CASCADE, blank = False)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)
    
class Departaments(models.Model):
    name = models.CharField(max_length = 10, blank = False)
    abrev = models.CharField(max_length = 10, blank = False)
    descript =  models.CharField(max_length = 10, blank = False)
    id_country = models.ForeignKey("Countries", on_delete = models.CASCADE, blank = False)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)
    
class Countries(models.Model):
    name = models.CharField(max_length = 10, blank = False)
    abrev = models.CharField(max_length = 10, blank = False)
    descript =  models.CharField(max_length = 10, blank = False)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null =True, blank = True)
    
    