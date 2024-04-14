from django.urls import path

from registration import views


app_name = 'registration'


urlpatterns = [
   path('', views.register, name='index'),
   path('login', views.login, name='login'),
   path('user', views.get_user, name='get_user'),
]
