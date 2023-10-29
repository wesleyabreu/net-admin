'''
Modelos usando Design Pattern Data Access Object (DAO).

Herda classe Model do Django, que implementa uma tabela
no banco de dados, inserindo atributos estáticos para 
serem as colunas da tabela modelada aqui.
'''
from django.db import models
from AdminFinanceiro.models import Plan


class Person(models.Model):
    """
    Modelo DAO da tabela Pessoa
    """
    name = models.CharField('Nome', max_length=32, default='')
    cpf = models.CharField('CPF', max_length=14, default='')
    rg = models.CharField('RG', max_length=14, default='')
    birthday = models.DateField('Data de Nascimento')
    address = models.CharField('Endereço', max_length=64, default='')


class Contract(models.Model):
    """
    Modelo DAO da tabela Contrato
    """
    subscription_date = models.DateField('Data de Assinatura')
    plan = models.ForeignKey(
        Plan, on_delete=models.DO_NOTHING, verbose_name='Plano')


class Schedule(models.Model):
    """
    Modelo DAO da tabela Agendamento
    """
    date = models.DateField('Data')
    hour = models.TimeField('Hora')


class Client(models.Model):
    """
    Modelo DAO da tabela Cliente
    """
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, verbose_name='Pessoa')
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, verbose_name='Contrato')
    install_date = models.ForeignKey(
        Schedule, on_delete=models.CASCADE, verbose_name='Data de Instalação')
