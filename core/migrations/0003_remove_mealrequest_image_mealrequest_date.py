# Generated by Django 5.1.4 on 2025-02-25 02:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_mealrequest_remove_requestsnack_user_delete_snack_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealrequest',
            name='image',
        ),
        migrations.AddField(
            model_name='mealrequest',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
