from django.urls import path
from note import views

urlpatterns = [
    path('note', views.note_home),
]
