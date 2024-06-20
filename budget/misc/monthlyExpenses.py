from datetime import datetime
from dateutil.relativedelta import relativedelta
from budget.misc.misc_funcs import filter_ledger_items, calc_total_amount

class MonthlyExpenses:
    """Class to compile twelve months of data for budgeted and actual amounts"""
    def __init__(self, budget_items, ledger_items):
        self.budget_items = budget_items
        self.ledger_items = ledger_items
        self.data = {
            'periods': [],
            'labels': [],
            'actuals': [],
            'budget_total': 0,
        }

    def compile(self):
        """Compiles all data"""
        self.compile_periods()
        self.compile_ledger_items()
        self.data['budget_total'] = calc_total_amount(self.budget_items)

    def compile_ledger_items(self):
        """Compiles total actual expenses for last 12 months"""
        for period in self.data['periods']:
            params = {'month': period.month, 'year': period.year}
            ledger_items = filter_ledger_items(self.ledger_items, params)
            self.data['actuals'].append(calc_total_amount(ledger_items))        

    def compile_periods(self):
        """Returns a list of last 12 month/year pairs"""
        current_date = datetime.now()
        for i in range(1, 7):
            new_date = current_date - relativedelta(months=i)
            self.data['periods'].insert(0, new_date)
            self.data['labels'].insert(0, self.get_period_label(new_date))

    def get_period_label(self, date):
        """Return full month name of given datetime object"""
        return date.strftime("%b-%y")