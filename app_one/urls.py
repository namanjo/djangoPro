from app_one import views
from django.urls import path


#For template tagging
app_name = 'app_one'


urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup/', views.sign_up, name = 'sign_up'),
]
