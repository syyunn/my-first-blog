#model is a bridge between django and database. 
## it operates django how to interact with its database.

from django.db import models
from django.utils import timezone

class Post(models.Model): #models imported from django.db 

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #this is link to antoehr model    
    title = models.CharField(max_length=200) #models.** creates database table under given condition
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True) # null = True means it's okay to be blank, but others, be essentially defined.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


#class Graph

# Create your models here.
