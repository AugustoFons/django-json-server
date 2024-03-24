"""
URL configuration for jsonDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from carrito.views import carrito_prod, favoritos_prod

urlpatterns = [
    path('', views.index, name='index'),
    path('productosSmartphone/', views.index, name='productos_smartphone'),
    path('productosTvs/', views.index, name='productos_tvs'),
    path('productosAudio/', views.index, name='productos_audio'),
    path('productosDestacados/', views.index, name='productos_destacados'),
    path('carrito/', carrito_prod, name='carrito'),
    path('carrito/<int:producto_id>/', carrito_prod, name='editar_eliminar_carrito'),
    path('favoritos/', favoritos_prod, name='favoritos'),
    path('favoritos/<int:favoritos_id>/', favoritos_prod, name='eliminar_favoritos')
]
