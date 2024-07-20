from django.contrib import admin

# Register your models here.
from .models import Post

#to add this model to admin panel
admin.site.register(Post)
