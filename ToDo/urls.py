from django.urls import path

from ToDo import views

urlpatterns = [
    path('', views.start),
]