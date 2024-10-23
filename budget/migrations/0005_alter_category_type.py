# Generated by Django 4.2.11 on 2024-09-09 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_alter_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('Expense', 'Expense'), ('Fixed_Expense', 'Fixed_Expense'), ('Variable_Expense', 'Variable_Expense'), ('Income', 'Income')], default='Expense', max_length=20),
        ),
    ]