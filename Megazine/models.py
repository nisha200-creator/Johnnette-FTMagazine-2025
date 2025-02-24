from django.db import models

class HomeArticle(models.Model):
    image = models.ImageField(upload_to="articles/", height_field=None, width_field=None, max_length=255)
    title = models.CharField(max_length=255)  

    def __str__(self):
        return self.title 
    







# Create your models here.

