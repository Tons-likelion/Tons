from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('<int:category_id>/', views.cat_detail, name="cat_detail"),
]

