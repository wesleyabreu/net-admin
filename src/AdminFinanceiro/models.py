"""
Modelos usando Design Pattern Data Access Object (DAO).

Herda classe Model do Django, que implementa uma tabela
no banco de dados, inserindo atributos estáticos para 
serem as colunas da tabela modelada aqui.
"""
from django.db import models


class Plan(models.Model):
    """
    Modelo DAO da tabela Plano de Assinatura
    """
    name = models.CharField('Nome do plano', max_length=32, default="")
    price = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0.0)
