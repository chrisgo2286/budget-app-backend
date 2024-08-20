from datetime import date
import calendar
from django.db.models import Sum

class MonthlySavingsChart:
    def __init__(self, month, year, items):
        self.month = month
        self.year = year
        self.expense_items, self.income_items = self.filter_items(items)
        self.data = []

    def compile(self):
        """Compiles month names and total expenses for each month"""
        current_month = self.month
        for i in range(6):
            amount = self.calc_monthly_savings(current_month)
            month_name = calendar.month_name[current_month]
            self.data.append({"name": month_name, "amount": amount})
    
    def calc_monthly_savings(self, month_num):
        """Returns savings for given month number"""
        expenses = self.calc_monthly_total(month_num, self.expense_items)
        income = self.calc_monthly_total(month_num, self.income_items)
        return income - expenses
    
    def calc_monthly_total(self, month_num, items):
        """Returns amount total for given month in given items"""
        filtered_items = items.filter(month=month_num)
        amount_sum = filtered_items.aggregate(Sum("amount"))
        return float(amount_sum["amount__sum"])
    
    def filter_items(self, items):
        """Returns queryset of expenses and queryset of income items"""
        current_date = date.today()
        current_items = items.filter(date__lte=current_date)
        expense_items = current_items.filter(category__type="Expense")
        income_items = current_items.filter(category__type="Income")
        return expense_items, income_items