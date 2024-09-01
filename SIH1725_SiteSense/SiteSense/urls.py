from django.urls import path
from . import views

urlpatterns = [
    path('', views.entrance, name='entrance'),
    path('errorCheckpoint/', views.errorCheckpoint, name='errorCheckpoint'),
    path('home/', views.home, name='home'),
    path('imagehub/', views.imagehub, name='imagehub'),
    path('login/', views.login, name='login'),
    path('progress/', views.progress, name='progress'),
    path('register/', views.register, name='register'),
    path('stageInsight/', views.stageInsight, name='stageInsight'),
]
