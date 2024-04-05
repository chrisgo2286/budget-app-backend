from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .serializers import (CategorySerializer, LedgerItemSerializer, 
    BudgetItemSerializer)
from .models import Category, LedgerItem, BudgetItem
from .misc.budget_data import BudgetData

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

    def create(self, request):
        category = request.data.get('category')
        category_type = request.data.get('type')
        amount = request.data.get('amount')
        user = User.objects.get(id=request.user.id)
    
        new_category = Category(owner=user, name=category, type=category_type)
        new_category.save()

        budget_item = BudgetItem(owner=user, category=new_category,
            amount=amount)
        budget_item.save()

        return Response(status=200)

@api_view(('GET',))
def ledger_view(request):
    user = User.objects.get(id=request.user.id)
    queryset = LedgerItem.objects.filter(owner=user)
    queryset = queryset.values('id', 'date', 'category__name', 
        'category__type', 'amount')
    return(Response(queryset))

@api_view(('GET',))
def budget_view(request):
    user = User.objects.get(id=request.user.id)
    budget_items = BudgetItem.objects.filter(owner=user)
    ledger_items = LedgerItem.objects.filter(owner=user)
    budget = BudgetData(budget_items, ledger_items)
    budget.compile()
    return(Response(budget.data))
