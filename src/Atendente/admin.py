from django.contrib import admin
from .models import Person, Contract, Schedule, Client

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "cpf")

admin.site.register(Person, PersonAdmin)
admin.site.register(Contract)
admin.site.register(Schedule)
admin.site.register(Client)