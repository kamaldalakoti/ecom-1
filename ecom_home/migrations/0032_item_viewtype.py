# Generated by Django 2.2.14 on 2020-12-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_home', '0031_remove_item_viewtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ViewType',
            field=models.IntegerField(default=2),
        ),
    ]
