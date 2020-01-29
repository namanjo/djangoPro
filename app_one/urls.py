from app_one import views
from django.urls import path


urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup/', views.sign_up, name = 'sign_up'),
]
