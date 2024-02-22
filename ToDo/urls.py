from django.urls import path

from ToDo import views

urlpatterns = [
    path('', views.start),
    path('all_users/', views.all_users),
    path('user/<int:user_id>/', views.pers_user),
]