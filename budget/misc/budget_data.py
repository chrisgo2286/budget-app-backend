from budget.misc.filters import Filters

class BudgetData:
    """Compiles required data for Budget Page"""
    def __init__(self, budget_items, ledger_items, month=None, year=None):
        self.month = month
        self.year = year
        self.budget_items = budget_items
        self.ledger_items = self.filter_ledger_items(ledger_items)
        self.data = []

    def compile(self):
        """Populates data list"""
        for budget_item in self.budget_items:
            id = budget_item.id
            category = budget_item.category.name
            category_type = budget_item.category.type
            budget_amount = budget_item.amount
            actual_amount = self.calc_actual_amount(category)
            percent = self.calc_percent(actual_amount, budget_amount)
            
            self.data.append({
                'id':id,
                'category':category,
                'type': category_type,
                'budget_amount': budget_amount,
                'actual_amount': actual_amount,
                'percent': percent
            })

    def calc_actual_amount(self, category):
        """Returns the actual amount for given category"""
        total = 0
        for ledger_item in self.ledger_items:
            if ledger_item.category.name == category:
                total += ledger_item.amount
        return total

    def calc_percent(self, actual, total):
        """Returns percent of actual over budget amount"""
        decimal = round(actual / total, 2)
        return f'{decimal * 100}%'
    
    # Filter LedgerItems
    def filter_ledger_items(self, ledger_items):
        """Filters ledger items by month and year"""
        self.filters = Filters(ledger_items, self.month, self.year)
        self.filters.filter_queryset()
        return self.filters.queryset