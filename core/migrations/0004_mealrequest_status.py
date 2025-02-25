# Generated by Django 5.1.4 on 2025-02-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_mealrequest_image_mealrequest_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealrequest',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('deferido', 'Deferido'), ('indeferido', 'Indeferido')], default='pendente', max_length=10),
        ),
    ]
