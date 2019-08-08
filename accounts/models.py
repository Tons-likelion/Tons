from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from category.models import Category

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField()
    obj_sum = models.ManyToManyField('article.Summary', blank=True, related_name='obj_users')
    sbj_sum = models.ManyToManyField('article.Summary', blank=True, related_name='sbj_users')
    category = models.ManyToManyField(Category, blank=True)
    
    def __str__(self):
        return self.user.username

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()