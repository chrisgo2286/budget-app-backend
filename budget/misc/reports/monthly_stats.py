from datetime import date
from django.db.models import Sum

class MonthlyStats:
    def __init__(self, month, year, items, budget):
        self.items = self.filter_ledger_items(items, month, year)
        self.budget = self.filter_budget_items(budget, month, year)
        self.data = {
            "expenses": 0,
            "income": 0,
            "savings": 0,
            "budgetPercent": 0
        }

    def compile(self):
        """Compiles all stats into data dict"""
        self.calc_expenses_and_income()
        self.calc_savings()
        self.calc_percent_of_budget()

    def calc_expenses_and_income(self):
        """Calculates total expenses for given period"""
        print(self.items)
        for item in self.items:
            if item.category.type in ("Fixed_Expense", "Variable_Expense"):
                self.data["expenses"] += float(item.amount)
            else:
                self.data["income"] += float(item.amount)

    def calc_savings(self):
        """Calculates savings for given period"""
        self.data["savings"] = self.data["income"] - self.data["expenses"] 
    
    def calc_percent_of_budget(self):
        """Calculates expenses as percent of budget"""
        total_budget = self.calc_budget_total()
        if total_budget > 0:
            percent = round(self.data["expenses"] / total_budget * 100, 2)
            self.data["budgetPercent"] = percent

    def calc_budget_total(self):
        """Returns total for budget items"""
        budget_sum = self.budget.aggregate(Sum('amount'))
        if budget_sum["amount__sum"]:
            return float(budget_sum["amount__sum"])
        return 0.0

    def filter_budget_items(self, items, month, year):
        """Returns queryset of budget items based on month and year"""
        items = items.filter(month=month, year=year)
        return (
            items.filter(category__type="Fixed_Expense") |
            items.filter(category__type="Variable_Expense")    
        )
    
    def filter_ledger_items(self, items, month, year):
        """Returns queryset of current runs based on month and year"""
        current_date = date.today()
        return items.filter(date__lte=current_date, date__month=month, 
            date__year=year)