from django.db import models
from django.db.models import Max
import random
# Create your models here.
class Category(models.Model):
    name = models.TextField(max_length=10,default='')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"