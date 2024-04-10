class Filters:
    """Class to filter BudgetItems"""
    def __init__(self, queryset, **params):
        self.queryset = queryset
        self.params = params
        self.filters = {
            'month': self.filter_month,
            'year': self.filter_year,
            'startDate': self.filter_start_date,
            'endDate': self.filter_end_date,
            'category': self.filter_category,
            'type': self.filter_type            
        }

    def filter_queryset(self):
        """Filters queryset based on provided parameters"""
        for key, value in self.params.items():
            if type(value) is list:
                value = value[0]    
            if value:
                self.filters[key](value)

    def filter_month(self, month):
        """Filters queryset for the given month"""
        self.queryset = self.queryset.filter(date__month=month)

    def filter_year(self, year):
        """Filters queryset for the given year"""
        self.queryset = self.queryset.filter(date__year=year)

    def filter_start_date(self, start_date):
        """Filters queryset for the given start date"""
        self.queryset = self.queryset.filter(date__gte=start_date)

    def filter_end_date(self, end_date):
        """Filters queryset for the given end date"""
        self.queryset = self.queryset.filter(date__lte=end_date)
    
    def filter_category(self, category):
        """Filters queryset for the given category"""
        self.queryset = self.queryset.filter(category=category)

    def filter_type(self, item_type):
        """Filters queryset for the given category type"""
        self.queryset = self.queryset.filter(category__type=item_type)