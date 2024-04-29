from budget.misc.filters import Filters
from budget.models import BudgetItem, LedgerItem

def budget_items(user):
    queryset = BudgetItem.objects.filter(user)
    print(queryset)
    return queryset

def test_func(budget_items):
    assert len(budget_items) > 0