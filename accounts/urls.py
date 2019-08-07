from django.urls import path, include
from . import views as accounts_views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', accounts_views.logout, name='logout'),
]