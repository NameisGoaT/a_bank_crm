# Generated by Django 5.0.3 on 2024-05-29 06:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_employees_changed_by_historicalemployees_changed_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='changed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='changed_by_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
