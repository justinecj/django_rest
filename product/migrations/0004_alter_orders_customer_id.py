# Generated by Django 4.2.5 on 2023-09-07 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_customer_preference_preference_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='customer_id',
            field=models.CharField(max_length=10),
        ),
    ]
