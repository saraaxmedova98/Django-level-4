from django.urls import path
from modelsTask import views
urlpatterns = [
    path('', views.home , name='home'),
]
