from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    image = models.URLField()
    address = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.image} {self.user} {self.address}"
    
class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.URLField()
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.image} {self.user} {self.address}"
    
class Comment(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.time_stamp} {self.content} {self.post}"
    

class PostViewRecord(models.Model):
    time_stamp = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} {self.post} {self.time_stamp}"

class Like(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} {self.post}"
