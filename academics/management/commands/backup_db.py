from django.core.management.base import BaseCommand
from  django.contrib.auth.models import User

import json

class Command(BaseCommand):
    #Config help impformation
    help = 'Meke a database backup in JSPM format'
    
    def handle(self, *args, **options):
        #Get data from User model
        users = User.objects.all()
        
        #Conver data to dictionaries
        data = [
            {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'password': user.password
            
            }
            for user in users
        ]
        
        #Save to Json format
        with open('backup_db.json','w') as file:
            json.dump(data, file, indent=4 )