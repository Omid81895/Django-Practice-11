from django.urls import path
from . import views
urlpatterns = [
    path('main/', views.todolist, name = 'home'),
    path('add/', views.add, name = 'add'),
    path('change/<str:id>/', views.change, name = 'change'),
]