from budget.misc.misc_funcs import calc_monthly_savings
from budget.misc.monthlyExpenses import MonthlyExpenses

class Reports:
    """Class to compile all reports for views"""
    def __init__(self, budget_items, ledger_items):
        self.budget_items = budget_items
        self.ledger_items = ledger_items
        self.data = {}

    def compile(self):
        """Compiles all report data"""
        self.compile_monthly_expenses()
        self.compile_monthly_savings()

    def compile_monthly_expenses(self):
        """Compiles monthly expense data"""
        expenses = MonthlyExpenses(self.budget_items, self.ledger_items)
        expenses.compile()
        self.data['monthlyExpense'] = expenses.data

    def compile_monthly_savings(self):
        """Compiles monthly savings data"""
        savings = calc_monthly_savings(self.data['monthlyExpense']['actuals'],
            self.data['monthlyExpense']['budget_total'])
        labels = self.data['monthlyExpense']['labels']
        self.data['monthlySavings'] = {'savings': savings, 'labels': labels}