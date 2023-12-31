from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastrar_comida/', cadastrar_comida, name='cadastrar_comida'),
    path('excluir_comida/<int:id_comida>', excluir_comida, name='excluir_comida'),
    path('logar/', logar, name='logar'),
    path('pagina_inicial/', pagina_inicial, name='pagina_inicial'),
    path('deslogar/', deslogar, name='deslogar'),
    path('listar_pedido/', listar_pedido, name='listar_pedido'),
    path('cadastrar_categoria/', cadastrar_categoria, name='cadastrar_categoria'),
    path('editar_categoria/<int:id_categoria>/', editar_categoria, name='editar_categoria'),
    path('editar_comida/<int:id_comida>/', editar_comida, name='editar_comida'),
    path('fechar_pedido/<int:id_pedido>', fechar_pedido, name='fechar_pedido'),
    path('comidanpedido/', comidanpedido, name='comidanpedido'),
    path('cadastrar_garcom/', cadastrar_garcom, name="cadastrar_garcom"),
    path('exibir_categoria/', exibir_categorias, name='exibir_categoria'),
    path('excluir_categoria/<int:id_categoria>/', excluir_categoria, name='excluir_categoria'),
    path('criar_pedido', criar_pedido, name='criar_pedido'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)