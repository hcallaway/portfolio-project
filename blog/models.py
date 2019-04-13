from django.db import models

# Create your models here.
class Blog(models.Model):
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=200)
    body = models.TextField()