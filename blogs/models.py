from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
class Tags(models.Model):
    tags = models.CharField(max_length=200)
    
    def __str__(self):
        return self.tags

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50) 
    author_bio = models.TextField(max_length=300)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name()}"

class SparksModel(models.Model):
  
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=300)
    rating = models.IntegerField(validators=(MinValueValidator(1),MaxValueValidator(10))) 
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    date = models.DateField(null=True,auto_now=True)
    image = models.ImageField(upload_to="images/")
    content = models.TextField(max_length=2000)
    tags = models.ManyToManyField(Tags)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Blog Rating: {self.rating}'
    
class Comment(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField(max_length=300)
    post = models.ForeignKey(SparksModel,on_delete=models.CASCADE, related_name="comments")
    


