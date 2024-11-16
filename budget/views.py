from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from budget.serializers import (CategorySerializer, LedgerItemSerializer, 
    BudgetItemSerializer)
from budget.models import Category, LedgerItem, BudgetItem
from budget.misc.budget_data import BudgetData
from budget.misc.filters import Filters
from .misc.reports.monthly_stats import MonthlyStats
from .misc.reports.yearly_stats import YearlyStats
from .misc.reports.current_expense_chart import CurrentExpenseChart
from .misc.reports.monthly_expense_chart import MonthlyExpenseChart
from .misc.reports.monthly_savings_chart import MonthlySavingsChart
from budget.misc.budget_copy import BudgetCopy

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class LedgerItemView(viewsets.ModelViewSet):
    serializer_class = LedgerItemSerializer
    queryset = LedgerItem.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class BudgetItemView(viewsets.ModelViewSet):
    serializer_class = BudgetItemSerializer
    queryset = BudgetItem.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

@api_view(('GET',))
def ledger_view(request):
    user = User.objects.get(id=request.user.id)
    queryset = LedgerItem.objects.filter(owner=user)
    filters = Filters(queryset, **request.query_params)
    filters.filter_queryset()
    queryset = filters.queryset.order_by("date")
    values = queryset.values('id', 'date', 'category__name', 
        'category__type', 'amount')    
    return(Response(values))

@api_view(('GET',))
def budget_view(request):
    month = request.query_params['month']
    year = request.query_params['year']
    user = User.objects.get(id=request.user.id)
    budget_items = BudgetItem.objects.filter(owner=user)
    ledger_items = LedgerItem.objects.filter(owner=user)
    budget = BudgetData(budget_items, ledger_items, month, year)
    budget.compile()
    return(Response(budget.data))

@api_view(('GET',))
def monthly_stats_view(request):
    month = request.query_params['month']
    year = request.query_params['year']
    user = User.objects.get(id=request.user.id)
    ledger_items = LedgerItem.objects.filter(owner=user)
    budget_items = BudgetItem.objects.filter(owner=user)
    monthly_stats = MonthlyStats(month, year, ledger_items, budget_items)
    monthly_stats.compile()
    return(Response(monthly_stats.data))

@api_view(('GET',))
def yearly_stats_view(request):
    year = request.query_params['year']
    user = User.objects.get(id=request.user.id)
    ledger_items = LedgerItem.objects.filter(owner=user)
    budget_items = BudgetItem.objects.filter(owner=user)
    yearly_stats = YearlyStats(year, ledger_items, budget_items)
    yearly_stats.compile()
    return(Response(yearly_stats.data))

@api_view(('GET',))
def current_expense_chart_view(request):
    month = request.query_params['month']
    year = request.query_params['year']
    user = User.objects.get(id=request.user.id)
    ledger_items = LedgerItem.objects.filter(owner=user)
    categories = Category.objects.filter(owner=user)
    current_expense_chart = CurrentExpenseChart(month, year, ledger_items, categories)
    current_expense_chart.compile()
    return(Response(current_expense_chart.data))

@api_view(('GET',))
def monthly_expense_chart_view(request):
    month = request.query_params['month']
    year = request.query_params['year']
    user = User.objects.get(id=request.user.id)
    ledger_items = LedgerItem.objects.filter(owner=user)
    monthly_expense_chart = MonthlyExpenseChart(month, year, ledger_items)
    monthly_expense_chart.compile()
    return(Response(monthly_expense_chart.data))

@api_view(('GET',))
def monthly_savings_chart_view(request):
    month = request.query_params['month']
    year = request.query_params['year']
    user = User.objects.get(id=request.user.id)
    ledger_items = LedgerItem.objects.filter(owner=user)
    monthly_savings_chart = MonthlySavingsChart(month, year, ledger_items)
    monthly_savings_chart.compile()
    return(Response(monthly_savings_chart.data))

@api_view(('GET',))
def budget_copy_view(request):
    month = request.query_params['month']
    year = request.query_params['year']
    user = User.objects.get(id=request.user.id)
    budget_items = BudgetItem.objects.filter(owner=user)
    budget_copy = BudgetCopy(budget_items, month, year)
    budget_copy.copy()
    return(Response())