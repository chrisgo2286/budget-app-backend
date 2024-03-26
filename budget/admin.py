from django.contrib import admin
from .models import Category, LedgerItem, BudgetItem

# Register your models here.
admin.site.register(Category)
admin.site.register(LedgerItem)
admin.site.register(BudgetItem)