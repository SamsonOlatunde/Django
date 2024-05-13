from django.urls import path
from jumia import views

urlpatterns = [
    path('home_jummy', views.home_jumia),
    path('author', views.author),
]