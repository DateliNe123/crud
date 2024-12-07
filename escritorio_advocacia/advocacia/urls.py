from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Cliente URLs
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('clientes/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:pk>/excluir/', views.excluir_cliente, name='excluir_cliente'),

    # Processo URLs
    path('processos/', views.lista_processos, name='lista_processos'),
    path('processos/adicionar/', views.adicionar_processo, name='adicionar_processo'),
    path('processos/<int:pk>/editar/', views.editar_processo, name='editar_processo'),
    path('processos/<int:pk>/excluir/', views.excluir_processo, name='excluir_processo'),
]