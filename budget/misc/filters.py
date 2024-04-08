class Filters:
    """Class to filter BudgetItems"""
    def __init__(self, queryset, month=None, year=None):
        self.queryset = queryset
        self.month = month
        self.year = year

    def filter_queryset(self):
        """Filters queryset based on provided parameters"""
        if(self.month):
            self.filter_month()

        if(self.year):    
            self.filter_year()

    def filter_month(self):
        """Filters queryset for the given month"""
        self.queryset = self.queryset.filter(date__month = self.month)

    def filter_year(self):
        """Filters queryset for hte given year"""
        self.queryset = self.queryset.filter(date__year = self.year)