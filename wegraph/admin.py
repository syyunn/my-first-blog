from django.contrib import admin
from .models import Post

admin.site.register(Post) # this makes our model (POST) visible on the admin page

# Register your models here.
