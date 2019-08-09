from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('<int:article_id>/', views.detail, name="detail"),
    path('<int:article_id>/summary/', views.summary, name="summary"),
    path('summary_obj/<int:summary_id>/', views.summary_obj, name="summary_obj"),
    path('summary_sbj/<int:summary_id>/', views.summary_sbj, name="summary_sbj"),
    path('<int:article_id>/stars/', views.stars, name="stars"),
]