from budget.misc.filters import Filters

def filter_ledger_items(ledger_items, params):
    """Filters ledger items by month and year"""
    filters = Filters(ledger_items, params)
    filters.filter_queryset()
    return filters.queryset

def calc_actual_amount(ledger_items, category):
    """Returns the actual amount for given category"""
    return sum([
            item.amount for item in ledger_items 
            if item.category == category
        ])
    
    # total = 0
    # for ledger_item in ledger_items:
    #     if ledger_item.category.name == category:
    #         total += ledger_item.amount
    # return total

def calc_total_amount(ledger_items):
    """Returns the total actual amount for give ledger_items"""
    return sum([item.amount for item in ledger_items])