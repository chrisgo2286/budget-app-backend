from datetime import date
from dateutil.relativedelta import relativedelta
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
        current_date = date(int(self.year), int(self.month), 1)
        for _ in range(5):
            amount = self.calc_monthly_sum(current_date.month)
            month_name = calendar.month_name[current_date.month][:3]
            self.data.insert(0, {"name": month_name, "amount": amount})
            current_date = current_date - relativedelta(months=1)

    def filter_expense_items(self, items):
        """Filters current items for only expense type"""
        current_date = date.today()
        return items.filter(date__lte=current_date, category__type="Expense")
    
    def calc_monthly_sum(self, month_num):
        """Returns amount total"""
        items = self.items.filter(date__month=month_num)
        if items:
            amount_sum = items.aggregate(Sum("amount"))
            return float(amount_sum["amount__sum"])
        return 0.0
        