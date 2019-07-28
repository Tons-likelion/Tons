from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('<int:article_id>/', views.detail, name="detail"),
    path('<int:article_id>/summary', views.summary, name="summary"),
]