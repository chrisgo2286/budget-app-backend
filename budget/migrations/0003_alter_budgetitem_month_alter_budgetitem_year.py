# Generated by Django 4.2.11 on 2024-09-06 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_budgetitem_month_budgetitem_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetitem',
            name='month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='budgetitem',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
