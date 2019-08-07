"""Tons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import Tons.views
import category.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Tons.views.home, name='home'),

    path('mypage/<int:user_id>/', category.views.mypage, name='mypage'),

    path('article/', include('article.urls')),
    path('accounts/', include('accounts.urls')),

    # path('cat_detail', base_app.views.category_detail, name='cat_detail'), #추후 url 수정 필요

]
