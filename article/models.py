from django.db import models
from django.utils import timezone
from category.models import Category
# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = True)
    content = models.TextField()
    stars = models.FloatField(default=0)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    class Meta:
        ordering = ['-id'] #최신순 #TODO: 별점순 바꾸기

class Summary(models.Model):
    belongsto_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    obj_count = models.PositiveIntegerField(default=0) #객관지수
    sbj_count = models.PositiveIntegerField(default=0)  #주관지수

    def __str__(self):
        return self.content
        
    class Meta:
        ordering = ['-id'] #최신순