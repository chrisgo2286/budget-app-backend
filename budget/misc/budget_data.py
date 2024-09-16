from budget.misc.filters import Filters

class BudgetData:
    """Compiles required data for Budget Page"""
    def __init__(self, budget_items, ledger_items, month=None, year=None):
        self.month = month
        self.year = year
        self.budget_items = self.filter_budget_items(budget_items)
        self.ledger_items = self.filter_ledger_items(ledger_items)
        self.budget_total = 0
        self.ledger_total = 0
        self.data = {
            "variable_expense": {
                "budget": 0,
                "ledger": 0
            },
            "fixed_expense": {
                "budget": 0,
                "ledger": 0
            },
            "expense": {
                "budget": 0,
                "ledger": 0,
                "percent": 0,
            },
            "income": {
                "budget": 0,
                "ledger": 0,
                "percent": 0
            },
            "items": []
        }

    def compile(self):
        """Populates data list"""
        for budget_item in self.budget_items:
            try:
                id = budget_item.id
                category = budget_item.category.name
                category_type = budget_item.category.type
                budget_amount = budget_item.amount
                actual_amount = self.calc_actual_amount(category)
                percent = self.calc_percent(actual_amount, budget_amount)
                
                self.data["items"].append({
                    'id':id,
                    'category':category,
                    'type': category_type,
                    'budget_amount': budget_amount,
                    'actual_amount': actual_amount,
                    'percent': percent
                })

                self.data[category_type.lower()]["budget"] += budget_amount
                self.data[category_type.lower()]["ledger"] += actual_amount

            except:
                pass

        expense_budget = self.data["fixed_expense"]["budget"] + self.data["variable_expense"]["budget"]
        expense_ledger = self.data["fixed_expense"]["ledger"] + self.data["variable_expense"]["ledger"]
        self.data["expense"]["budget"] = expense_budget
        self.data["expense"]["ledger"] = expense_ledger
        self.data["expense"]["percent"] = self.calc_percent(expense_ledger, expense_budget)
        self.data["income"]["percent"] = self.calc_percent(self.data["income"]["ledger"], self.data["income"]["budget"])

    def calc_actual_amount(self, category):
        """Returns the actual amount for given category"""
        total = 0
        for ledger_item in self.ledger_items:
            if ledger_item.category.name == category:
                total += ledger_item.amount
        return total

    def calc_percent(self, actual, total):
        """Returns percent of actual over budget amount"""
        if total:
            decimal = round(actual / total, 2)
            return f'{decimal * 100}%'
        return 0.0
    
    # Filter LedgerItems and BudgetItems
    def filter_ledger_items(self, items):
        """Filters ledger items by month and year"""
        return items.filter(date__month=self.month, date__year=self.year)
    
    def filter_budget_items(self, items):
        """Filters budget items by month and year"""
        return items.filter(month=self.month, year=self.year)