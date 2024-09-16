from django.urls import path
from . import views

app_name = 'blogb'


urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:post>/', views.single_post, name='single_post'),
]