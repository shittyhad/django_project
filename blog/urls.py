from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="blog-home"),
    path('colony/', views.colony, name="colony-home"),
    
]
