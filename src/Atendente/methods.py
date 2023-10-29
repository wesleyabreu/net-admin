"""
Abstração de métodos usados nas views (controllers) do CRUD do Atendente.
"""
from . import models
from datetime import datetime


def create_client(name, cpf, rg, birthday, address, install_date, install_hour, plan_id):
    """
    Cadastra um Cliente na base de dados (CREATE).
    """
    person = models.Person()
    person.name = name
    person.cpf = cpf
    person.rg = rg
    person.birthday = birthday
    person.address = address
    person.save()

    installation = models.Schedule()
    installation.date = install_date
    installation.hour = install_hour
    installation.save()

    contract = models.Contract()
    contract.subscription_date = datetime.now()
    contract.plan = models.Plan.objects.get(id=plan_id)
    contract.save()

    client = models.Client()
    client.person = person
    client.install_date = installation
    client.contract = contract
    client.save()


def list_all_clients():
    """
    Lista todos os Clientes cadastrados na base de dados (READ).
    """
    return models.Client.objects.all()


def update_client(client, posted_plan_id, name, cpf, rg, birthday, address):
    """
    Modifica dados do cliente cadastrados na base de dados (UPDATE).
    """
    if posted_plan_id != client.contract.plan.id:
        # Altera o plano de assinatura
        contract = models.Contract()
        contract.subscription_date = datetime.now()
        contract.plan = models.Plan.objects.get(id=posted_plan_id)
        contract.save()

        client.contract.delete()
        client.contract = contract
        client.save()

    client.person.name = name
    client.person.cpf = cpf
    client.person.rg = rg
    client.person.birthday = birthday
    client.person.address = address
    client.person.save()


def delete_client_subscription(client):
    """
    Cancela a assinatura de um cliente (DELETE).
    """
    client.contract.delete()
    client.person.delete()
