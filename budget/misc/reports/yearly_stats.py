from datetime import date
from calendar import monthrange
from budget.models import BudgetItem
from django.db.models import Sum

class YearlyStats:
    def __init__(self, year, items, budget):
        self.items = self.filter_ledger_items(items, year)
        self.budget = self.filter_budget_items(budget, year)
        self.data = {
            "expenses": 0,
            "income": 0,
            "savings": 0,
            "budgetPercent": 0
        }

    def compile(self):
        """Compiles all stats into data dict"""
        print(f"Ledger: { self.items }")
        print(f"Budget: { self.budget }")
        self.calc_expenses_and_income()
        self.calc_savings()
        self.calc_percent_of_budget()

    def calc_expenses_and_income(self):
        """Calculates total expenses for given period"""
        for run in self.items:
            if run.category.type == "Expense":
                self.data["expenses"] += float(run.amount)
            else:
                self.data["income"] += float(run.amount)

    def calc_savings(self):
        """Calculates savings for given period"""
        self.data["savings"] = self.data["income"] - self.data["expenses"] 
    
    def calc_percent_of_budget(self):
        """Calculates expenses as percent of budget"""
        total_budget = self.calc_budget_total()
        print(f"Total Budget: {total_budget}")
        percent = round(self.data["expenses"] / total_budget * 100, 2)
        self.data["budgetPercent"] = percent
    
    def calc_budget_total(self):
        """Returns total for budget items"""
        budget_sum = self.budget.aggregate(Sum('amount'))
        return float(budget_sum["amount__sum"])
        
    def calc_total_months(self):
        """Returns total months as a float"""
        current_date = date.today()
        full_months = int(current_date.month)
        fraction_of_month = (current_date.day / monthrange(current_date.year, 
            current_date.month)[1])
        return full_months + fraction_of_month

    def filter_budget_items(self, items, year):
        """Returns queryset of budget items for given year"""
        return items.filter(year=year, category__type="Expense")
    
    def filter_ledger_items(self, items, year):
        """Returns queryset of current items based on month and year"""
        current_date = date.today()
        return items.filter(date__lte=current_date, date__year=year)