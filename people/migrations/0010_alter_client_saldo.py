# Generated by Django 4.2.1 on 2023-08-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_alter_product_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='saldo',
            field=models.PositiveSmallIntegerField(default=947),
        ),
    ]
