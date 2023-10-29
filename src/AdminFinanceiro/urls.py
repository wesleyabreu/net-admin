"""
Definição de rotas do CRUD do AdminFinanceiro.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-plano/', views.create_plan, name='create_plan'),
    path('modificar-plano/<int:id>/', views.update_plan, name='update_plan'),
    path('excluir-plano/<int:id>/', views.delete_plan, name='delete_plan'),
    path('listar-planos/', views.list_all_plans, name='list_all_plans'),
]
