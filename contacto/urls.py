from django.urls import path
from . import views

urlpatterns = [
     path('', views.contacto, name='contacto' ),
     path('add_contacto', views.add_contacto, name='add_contacto')
]