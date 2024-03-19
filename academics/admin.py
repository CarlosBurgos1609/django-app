from django.contrib import admin
from .models import User, Person, Students, Identification_types, Cities, Departaments, Countries
# Register your models here.

admin.site.register(User)
admin.site.register(Person)
admin.site.register(Students)
admin.site.register(Identification_types)
admin.site.register(Cities)
admin.site.register(Departaments)
admin.site.register(Countries)
