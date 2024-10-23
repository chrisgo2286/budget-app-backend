from datetime import datetime
from dateutil.relativedelta import relativedelta
from budget.models import BudgetItem

class BudgetCopy:
    """Class to copy budget from last month over to given month"""
    def __init__(self, budget_items, month, year):
        self.budget_items = budget_items
        self.month = int(month)
        self.year = int(year)

    def copy(self):
        """Copys previous month's budget items to current month"""
        items = self.filter_budget_items()
        self.create_new_budget_items(items)

    def filter_budget_items(self):
        """Filters budget items for previous month's budget items"""
        current_month = datetime(self.year, self.month, 1)
        previous_month = current_month - relativedelta(months=1)
        return self.budget_items.filter(month=previous_month.month,
            year=previous_month.year)

    def create_new_budget_items(self, items):
        """Creates new budget items for current month"""
        for item in items:
            self.create_item(item)

    def create_item(self, item):
        """Creates new budget item with current month and year"""
        BudgetItem.objects.create(
            owner=item.owner,
            category=item.category,
            amount=item.amount,
            month=self.month,
            year=self.year
        )