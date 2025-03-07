# Generated by Django 5.1.4 on 2025-02-25 01:56

import core.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_type', models.CharField(choices=[('jantar', 'Jantar'), ('almoco', 'Almoço')], max_length=10)),
                ('justification', models.CharField(choices=[('turno_inverso', 'Aula em turno inverso'), ('esporte', 'Práticas esportivas')], max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.get_file_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='requestsnack',
            name='user',
        ),
        migrations.DeleteModel(
            name='Snack',
        ),
        migrations.DeleteModel(
            name='RequestSnack',
        ),
    ]
