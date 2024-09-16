from datetime import date
from django.db.models import Sum

class CurrentExpenseChart:
    def __init__(self, month, year, items, categories):
        self.categories = categories
        self.items = self.filter_items_by_period(month, year, items)
        self.data = []

    def compile(self):
        """Compiles category names and respective totals for given month"""
        self.expense_categories = self.compile_expense_categories()
        self.compile_expense_totals()

    def compile_expense_categories(self):
        """Compiles list of all categories for given period for user"""
        return [category for category in self.categories 
            if category.type != "Income"]

    def compile_expense_totals(self):
        """Compiles totals for each category"""
        for category in self.expense_categories:
            amount = 0
            items = self.filter_items_by_category(category, self.items)
            if items:
                amount = self.calc_category_total(items)
            self.data.append({"name": category.name, "amount": amount})

    def filter_items_by_period(self, month, year, items):
        """Filters items for given period and for current items"""
        current_date = date.today()
        return items.filter(date__lte=current_date, date__month=month,
            date__year=year)

    def filter_items_by_category(self, category, items):
        """Filters items by given category"""
        return items.filter(category=category)
    
    def calc_category_total(self, items):
        """Return total for category for given items"""
        category_sum = items.aggregate(Sum("amount"))
        return float(category_sum["amount__sum"])