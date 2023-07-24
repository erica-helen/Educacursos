from django.urls import path
from . import views

app_name='cliente'

urlpatterns = [
    path('pesquisar/', views.pesquisar_cursos, name='pesquisar_cursos'),

    path('', views.home, name='home'),
    path('add/<int:id>', views.add, name='add'),
    path('informacao/<int:id>', views.informacao, name='informacao'),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.loginPage, name='logout')

]
