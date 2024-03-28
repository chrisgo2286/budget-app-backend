from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (CategorySerializer, LedgerItemSerializer, 
    BudgetItemSerializer)
from .models import Category, LedgerItem, BudgetItem

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class LedgerItemView(viewsets.ModelViewSet):
    serializer_class = LedgerItemSerializer
    queryset = LedgerItem.objects.all()

@api_view(('GET',))
def ledger_view(self):
    queryset = LedgerItem.objects.all().values('id', 'date', 'category__name', 
        'category__type', 'amount')
    return(Response(queryset))