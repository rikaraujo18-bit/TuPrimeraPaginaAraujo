from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from veterinaria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('agregar/cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar/mascota/', views.agregar_mascota, name='agregar_mascota'),
    path('agregar/consulta/', views.agregar_consulta, name='agregar_consulta'),
    path('buscar/', views.buscar_mascota, name='buscar'),
    path('accounts/', include('accounts.urls')),
    
    # CBV - Listado y detalle de mascotas
    path('mascotas/', views.ListadoMascotasView.as_view(), name='listado_mascotas'),
    path('mascotas/<int:pk>/', views.DetalleMascotaView.as_view(), name='detalle_mascota'),
    
    # FBV - Editar y eliminar (operaciones con formularios POST)
    path('mascotas/editar/<int:mascota_id>/', views.editar_mascota, name='editar_mascota'),
    path('mascotas/eliminar/<int:mascota_id>/', views.eliminar_mascota, name='eliminar_mascota'),
    
    # About
    path('about/', views.about, name='about'),
]

# Configuración para servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)