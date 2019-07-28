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
import base_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_app.views.home, name='home'),
    # path('base_app/', include('base_app.urls')),
    path('article/', include('article.urls')),
    path('signup/', base_app.views.signup, name="signup"),
    path('login/', base_app.views.login, name="login"),
    path('logout/', base_app.views.logout, name="logout"),
    path('mypage/', base_app.views.mypage, name="mypage"),
    path('summary_create/<int:article_id>/', base_app.views.summary_create, name="summary_create"),
    path('summary_delete/<int:article_id>/<int:sum_id>/', base_app.views.summary_delete, name="summary_delete"),
    path('summary_edit/<int:article_id>/<int:sum_id>/', base_app.views.summary_edit, name="summary_edit"),
]