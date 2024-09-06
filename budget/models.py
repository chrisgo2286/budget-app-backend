from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TYPE_CHOICES = (
    ('Expense', 'Expense'),
    ('Income', 'Income')
)

class Category(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length=20, 
        choices=TYPE_CHOICES, 
        default='Expense'
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name} ({self.type})'
    
class LedgerItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.category} - {self.amount}'
    
class BudgetItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.owner.id} - {self.category} - {self.amount} per Month'
