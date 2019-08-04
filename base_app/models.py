from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# 유저 저장
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField()
    phone_number = models.TextField(verbose_name="폰번호")


# 전부 크롤링해서 불러올 내용. 작성 불가.
class Article(models.Model):
    title = models.TextField()
    pub_date = models.DateTimeField()
    body = models.TextField()
    stars = models.IntegerField(default=0) #별점

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id'] #최신순


# 유저들이 올릴 요약 저장
class Summary(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    good = models.IntegerField(default=0) #객관지수
    bad = models.IntegerField(default=0)  #주관지수

    def __str__(self):
        return self.content
        
    class Meta:
        ordering = ['-id'] #최신순


#유저가 선택한 카테고리? 전체 카테고리?
class Category(models.Model):
    pass
