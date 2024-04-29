import pytest
from django.contrib.auth.models import User
from budget.models import BudgetItem, LedgerItem, Category

@pytest.fixture
def user():
    return User(username='tester', password='Cypress123')

@pytest.fixture
def category1(user):
    return Category(owner=user, name='Mortgage', type='Expense')

@pytest.fuxture
def category2(user):
    return Category(owner=user, name='Grocery', type='Expense')

@pytest.fixture
def category3(user):
    return Category(owner=user, name='Income', type='Income')

@pytest.fixture
def budget_item1(user, category1):
    return BudgetItem(owner=user, category=category1, amount='100')