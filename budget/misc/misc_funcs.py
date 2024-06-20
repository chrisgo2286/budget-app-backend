from budget.misc.filters import Filters

def filter_ledger_items(ledger_items, params):
    """Filters ledger items by month and year"""
    filters = Filters(ledger_items, **params)
    filters.filter_queryset()
    return filters.queryset

def calc_actual_amount(ledger_items, category):
    """Returns the actual amount for given category"""
    return sum([
            item.amount for item in ledger_items 
            if item.category == category
        ])

def calc_total_amount(items):
    """Returns the total actual amount for given ledger or budget items"""
    return sum([item.amount for item in items])

def calc_monthly_savings(actual_expenses, budget_total):
    return [(budget_total - expense) for expense in actual_expenses]