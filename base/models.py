from django.db import models

# Create your models here.
class ItemModel(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)