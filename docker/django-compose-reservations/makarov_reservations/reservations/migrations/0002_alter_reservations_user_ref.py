# Generated by Django 5.0.6 on 2024-06-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='user_ref',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
