from rest_framework import serializers
from .models import Category, LedgerItem, BudgetItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LedgerItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerItem
        fields = '__all__'

class BudgetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetItem
        fields = '__all__'