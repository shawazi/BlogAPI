from django.contrib import admin
from .models import *

# Register your models here.

data_models = (Blog, Profile, Category, Comment, Like, PostViewRecord)

admin.site.register(data_models)