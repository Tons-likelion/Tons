from django.contrib import admin
from .models import Author, Article, Summary, Category

# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Summary)
admin.site.register(Category)