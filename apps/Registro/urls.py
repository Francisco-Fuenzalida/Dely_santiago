from django.urls import path
from . import views

urlpatterns = [
    path('agregar_plato', views.agregar_plato, name='agregar_plato'),
    path('listado_platos', views.listar_platos, name='listado_platos'),
    path('editar_plato/<id>/', views.editar_plato, name='editar_plato'),
    path('eliminar_plato/<id>/', views.eliminar_plato, name='eliminar_plato'),
    path('agregar_proveedor', views.agregar_proveedor, name='agregar_proveedor'),
    path('listado_proveedores', views.listar_proveedor, name='listado_proveedores'),
    path('editar_proveedor/<id>/', views.editar_proveedor, name='editar_proveedor'),
    path('eliminar_proveedor/<id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('tienda', views.tienda, name='tienda'),
]