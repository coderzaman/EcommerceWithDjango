# Generated by Django 5.1.6 on 2025-02-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
