"""
Controles do CRUD do AdminFinanceiro.
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def create_plan(request):
    """
    Cria um Plano de Assinatura na base de dados (CREATE).

    :param request: Requisição HTTP processada do Django
    :return: Página HTML de criação do plano
    """
    if request.method == 'GET':
        return render(request, 'site/create_plan.html')

    if request.method == 'POST':
        plan = models.Plan()
        plan.name = request.POST['name']
        plan.price = request.POST['price']
        plan.save()
        return redirect('create_plan')

@login_required(login_url="/")
def list_all_plans(request):
    """
    Lista todos os Planos de Assinatura cadastrados na base de dados (READ).

    :param request: Requisição HTTP processada do Django
    :return: Página HTML de listagem de planos
    """
    if request.method == 'GET':
        plans = models.Plan.objects.all()
        return render(request, 'site/list_all_plans.html', context={'plans': plans})

@login_required(login_url="/")
def update_plan(request, id):
    """
    Modifica um Plano de Assinatura cadastrado na base de dados (UPDATE).

    :param request: Requisição HTTP processada do Django
    :param id: Chave no banco de dados do plano desejado
    :return: Página HTML de modificação do plano
    """
    plan = models.Plan.objects.get(id=id)

    if request.method == 'GET':
        return render(request, 'site/update_plan.html', context={'plan': plan})

    if request.method == 'POST':
        plan.name = request.POST['name']
        plan.price = request.POST['price']
        plan.save()
        return redirect('update_plan', id=id)

@login_required(login_url="/")
def delete_plan(request, id):
    """
    Exclui um Plano de Assinatura da base de dados (DELETE).

    :param request: Requisição HTTP processada do Django
    :param id: Chave no banco de dados do plano desejado
    :return: Resposta HTTP de conclusão da operação
    """
    if request.method == 'GET':
        plan = models.Plan.objects.get(id=id)
        plan.delete()
        return redirect('list_all_plans')
