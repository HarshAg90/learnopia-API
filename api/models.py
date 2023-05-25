from django.db import models

# Create your models.
class PostThumb(models.Model):
    name = models.CharField(max_length= 250)

class Entity(models.Model):
    # id = models.IntegerField()
    type = models.CharField(max_length=255)
    by_user = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    sem = models.CharField(max_length=255)
    topic = models.TextField()
    date = models.DateField(auto_now_add=True)
    image_index = models.CharField(max_length=255)
    embed_url = models.CharField(max_length=255)
    content_heading = models.CharField(max_length=255)
    content_body = models.TextField()
    redirect_link = models.CharField(max_length=255)