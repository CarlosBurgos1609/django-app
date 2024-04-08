from django.contrib import admin
from .models import User, identification_type, country, department, cities, person, student

# Register your models here
class UserFields(admin.ModelAdmin):
    list_display = ('email', 'password', 'status')
        
class PersonField(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'id_ident_type', 'id_ident_number')

admin.site.register(User, UserFields)
admin.site.register(identification_type)
admin.site.register(country)
admin.site.register(department)
admin.site.register(cities)
admin.site.register(person, PersonField )
admin.site.register(student)

