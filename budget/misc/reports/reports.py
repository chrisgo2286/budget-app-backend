from budget.models import BudgetItem, LedgerItem, Category
from budget.misc.reports.monthly_stats import MonthlyStats
from budget.misc.reports.yearly_stats import YearlyStats
from budget.misc.reports.current_expense_chart import CurrentExpenseChart
from budget.misc.reports.monthly_expense_chart import MonthlyExpenseChart
from budget.misc.reports.monthly_savings_chart import MonthlySavingsChart

class Reports:
    """Class to compile all reports for views"""
    def __init__(self, month, year, user):
        self.month = month
        self.year = year
        self.user = user
        self.ledger = LedgerItem.objects.filter(owner=user)
        self.budget = BudgetItem.objects.filter(owner=user)
        self.categories = Category.objects.filter(owner=user)
        self.data = {}

    def compile(self):
        """Compiles all report data"""
        self.compile_monthly_stats()
        self.compile_yearly_stats()
        self.compile_current_expenses()
        self.compile_monthly_expenses()
        self.compile_monthly_savings()
                
    def compile_monthly_stats(self):
        """Compiles monthly stats data"""
        monthly_stats = MonthlyStats(self.month, self.year, self.ledger, 
            self.budget)
        monthly_stats.compile()
        self.data["monthly_stats"] = monthly_stats.data

    def compile_yearly_stats(self):
        """Compiles yearly stats data"""
        yearly_stats = YearlyStats(self.year, self.ledger, self.budget)
        yearly_stats.compile()
        self.data["yearly_stats"] = yearly_stats.data

    def compile_current_expenses(self):
        """Compiles current expense data"""
        current_expense = CurrentExpenseChart(self.month, self.year, 
            self.ledger, self.categories)
        current_expenses.compile()
        self.data["current_expense_chart"] = current_expenses.data

    def compile_monthly_expenses(self):
        """Compiles monthly expense data"""
        monthly_expenses = MonthlyExpenses(self.budget, self.ledger)
        monthly_expenses.compile()
        self.data["monthly_expense_chart"] = monthly_expenses.data

    def compile_monthly_savings(self):
        """Compiles monthly savings data"""
        monthly_savings = MonthlySavingsChart(self.month, self.year, ledger)
        monthly_savings.compile()
        self.data["monthly_savings_chart"] = monthly_savings.data