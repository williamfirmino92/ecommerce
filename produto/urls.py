from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('', views.DetalheProduto.as_view(), name='detalhe'),
    path('', views.AdicionarAoCarrinho.as_view(), name='adicionarcarrinho'),
    path('', views.RemoverDoCarrinho.as_view(), name='removerdocarrinho'),
    path('', views.Carrinho.as_view(), name='carrinho'),
    path('', views.Finalizar.as_view(), name='finalizar'),   
]