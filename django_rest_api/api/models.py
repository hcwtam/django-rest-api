from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
