# Generated by Django 2.2.14 on 2020-12-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_home', '0018_auto_20201209_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_received',
            field=models.BooleanField(default=False),
        ),
    ]
