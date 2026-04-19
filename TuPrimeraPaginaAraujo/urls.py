from django.contrib import admin
from django.urls import path
from veterinaria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('agregar/cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar/mascota/', views.agregar_mascota, name='agregar_mascota'),
    path('agregar/consulta/', views.agregar_consulta, name='agregar_consulta'),
    path('buscar/', views.buscar_mascota, name='buscar'),
]