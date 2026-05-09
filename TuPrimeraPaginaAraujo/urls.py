from django.contrib import admin
from django.urls import path, include
from veterinaria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('agregar/cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar/mascota/', views.agregar_mascota, name='agregar_mascota'),
    path('agregar/consulta/', views.agregar_consulta, name='agregar_consulta'),
    path('buscar/', views.buscar_mascota, name='buscar'),
    path('accounts/', include('accounts.urls')),
    
    # NUEVAS RUTAS:
    path('mascotas/', views.listado_mascotas, name='listado_mascotas'),
    path('mascotas/<int:mascota_id>/', views.detalle_mascota, name='detalle_mascota'),
    path('mascotas/editar/<int:mascota_id>/', views.editar_mascota, name='editar_mascota'),
    path('mascotas/eliminar/<int:mascota_id>/', views.eliminar_mascota, name='eliminar_mascota'),
]