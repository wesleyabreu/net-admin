"""
Definição de rotas do CRUD do Atendente.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-cliente/', views.create_client, name='create_client'),
    path('modificar-cliente/<int:id>/', views.update_client, name='update_client'),
    path('cancelar-cliente/<int:id>/', views.delete_client_subscription, name='cancel_subscription'),
    path('listar-clientes/', views.list_all_clients, name='list_all_clients'),
]
