# Generated by Django 3.2.6 on 2021-12-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cart_compare_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('compare_date',)},
        ),
        migrations.AlterField(
            model_name='cart',
            name='compare_date',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
