from app_one import views
from django.urls import path


urlpatterns = [
    path('', views.index, name = 'index'),
    
]
