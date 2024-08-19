from datetime import date
from calendar import monthrange
from budget.models import BudgetItem
from django.db.models import Sum

class YearlyStats:
    def __init__(self, year, items):
        self.items = self.filter_items(items, year)
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
        for run in self.items:
            if run.category.type == "Expense":
                self.data["expenses"] += run.amount
            else:
                self.data["income"] += run.amount

    def calc_savings(self):
        """Calculates savings for given period"""
        self.data["savings"] = self.data["income"] - self.data["expenses"] 
    
    def calc_percent_of_budget(self):
        """Calculates expenses as percent of budget"""
        total_budget = self.calc_budget_total()
        return self.data["expenses"] / total_budget * 100
    
    def calc_budget_total(self):
        """Returns total for budget items"""
        budget_sum = BudgetItem.objects.aggregate(Sum('amount'))
        monthly_budget = float(budget_sum["amount__sum"])
        total_months = self.calc_total_months()
        return monthly_budget * total_months

    def calc_total_months(self):
        """Returns total months as a float"""
        current_date = date.today()
        full_months = current_date.month
        fraction_of_month = (current_date.day / monthrange(current_date.year, 
            current_date.month))
        return float(f'{full_months}.{fraction_of_month}')

    def filter_items(self, items, year):
        """Returns queryset of current items based on month and year"""
        current_date = date.today()
        return items.filter(date__lte=current_date, date__year=year)