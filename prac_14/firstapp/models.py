from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=True)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail',kwargs={'pk':self.pk})
