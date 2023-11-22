from django.contrib import admin
from .models import Plan

class PlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

admin.site.register(Plan, PlanAdmin)

