from django.db import models


# Create your models here.
class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.TextField()
    email = models.TextField()
    password = models.TextField()

class Post(models.Model):
    postid = models.IntegerField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    category = models.TextField()
    date_published = models.DateTimeField()

class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    postid = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    dateposted = models.DateTimeField()

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()