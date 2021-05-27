from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
  


class Gifs(models.Model):
    title = models.CharField(max_length=40)
    url = models.URLField()
    uploader_name = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name='gif_category')