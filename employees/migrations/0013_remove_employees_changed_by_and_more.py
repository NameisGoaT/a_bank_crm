# Generated by Django 5.0.3 on 2024-05-29 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0012_employees_changed_by_historicalemployees_changed_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='historicalemployees',
            name='changed_by',
        ),
    ]
