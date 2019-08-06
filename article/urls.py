from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('<int:article_id>/', views.detail, name="detail"),
    path('<int:article_id>/summary', views.summary, name="summary"),
    path('summary_obj_toggle/<int:summary_id>/', views.summary_obj_toggle, name="summary_obj_toggle"),
    path('summary_sbj_toggle/<int:summary_id>/', views.summary_sbj_toggle, name="summary_sbj_toggle"),
]