from rest_framework import viewsets
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