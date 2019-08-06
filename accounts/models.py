from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from article.models import Article, Summary

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10,default='')
    obj_summ = models.ManyToManyField(Summary, blank=True, related_name='obj_users')
    sbj_summ = models.ManyToManyField(Summary, blank=True, related_name='sbj_users')
    

    def __str__(self):
        return self.nickname

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    