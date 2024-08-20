from datetime import date
import calendar
from django.db.models import Sum

class MonthlyExpenseChart:
    def __init__(self, month, year, items):
        self.month = month
        self.year = year
        self.items = self.filter_expense_items(items)
        self.data = []

    def compile(self):
        """Compiles month names and total expenses for each month"""
        current_month = self.month
        for i in range(6):
            amount = self.calc_monthly_sum(current_month)
            month_name = calendar.month_name[current_month]
            self.data.append({"name": month_name, "amount": amount})

    def filter_expense_items(self, items):
        """Filters current items for only expense type"""
        current_date = date.today()
        return items.filter(date__lte=current_date, category__type="Expense")
    
    def calc_monthly_sum(self, month_num):
        """Returns amount total"""
        items = self.items.filter(month=month_num)
        amount_sum = items.aggregate(Sum("amount"))
        return float(amount_sum["amount__sum"])
        