# Generated by Django 2.2.14 on 2020-12-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_home', '0029_item_viewtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='ViewType',
            field=models.IntegerField(default=2),
        ),
    ]
