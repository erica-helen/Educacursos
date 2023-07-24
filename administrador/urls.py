from django.urls import path
from . import views

app_name='administrador'

urlpatterns = [
     path('', views.home, name='home'),
     path('add/', views.add, name='add'),
     path('del/<int:id>', views.delete, name='delete'),
     path('edit/<int:id>', views.edit, name='edit'),


]