from budget.models import BudgetItem, LedgerItem

class BudgetData:
    """Compiles required data for Budget Page"""
    def __init__(self, budget_items, ledger_items):
        self.budget_items = budget_items
        self.ledger_items = ledger_items
        self.data = []

    def compile(self):
        """Populates data list"""
        for budget_item in self.budget_items:
            id = budget_item.id
            category = budget_item.category.name
            budget_amount = budget_item.amount
            actual_amount = self.calc_actual_amount(category)
            percent = self.calc_percent(actual_amount, budget_amount)
            
            self.data.append({
                'id':id,
                'category':category,
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