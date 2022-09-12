from logging import PlaceHolder
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    thumbnail = models.ImageField(default='default.png',blank=True)
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(User,default=None,on_delete=CASCADE )


    def get_absolute_url(self):
        return f'/articles/'

    def __str__(self):
        return self.title
    def slim(self):
        return self.body[:50]+".........."



    