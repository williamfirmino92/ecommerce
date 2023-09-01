from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('produto.urls')),
    path('perfil/', include('perfil.urls')),
    path('pedido/', include('pedido.urls')),
    path('produto/', include('produto.urls')),
    path('admin/', admin.site.urls),
]
