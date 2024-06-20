from datetime import datetime
from dateutil.relativedelta import relativedelta
from misc_funcs import filter_ledger_items, calc_total_amount

class TwelveMonthExpenses:
    """Class to compile twelve months of data for budgeted and actual amounts"""
    def __init__(self, budget_items, ledger_items, month, year):
        self.month = month
        self.year = year
        self.budget_items = budget_items
        self.ledger_items = ledger_items
        self.actuals = []
        self.budgeted = []
        self.periods = []

    def compile(self):
        """Compiles all data"""
        self.compile_ledger_items()
        self.compile_budget_items()

    def compile_ledger_items(self):
        """Compiles total actual expenses for last 12 months"""
        for period in self.periods:
            params = {'month': period.month, 'year': period.year}
            ledger_items = filter_ledger_items(self.ledger_items, params)
            self.actuals.append(calc_total_amount(ledger_items))

    def compile_budget_items(self):
        """Compiles total budgeted expenses for last 12 months"""
        pass

    def compile_periods(self):
        """Returns a list of last 12 month/year pairs"""
        current_date = datetime.now()
        for i in range(13, 1):
            new_date = current_date - relativedelta(months=i)
            self.periods.append(new_date)
            current_date = new_date