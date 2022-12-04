from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.proveedores, name='proveedores' ),

    #Path to ADD Proveedor
    path('add_proveedor', views.add_proveedor, name="add_proveedor"),
    #Path to View  Proveedor data individually
    path('proveedor/<str:proveedor_id>', views.proveedor, name="proveedor"),
    #Path to EDIT Proveedor
    path('edit_proveedor', views.edit_proveedor, name="edit_proveedor"),
    #Path to DELETE Proveedor
    path('delete_proveedor/<str:proveedor_id>', views.delete_proveedor, name="delete_proveedor"),
    
   

]

