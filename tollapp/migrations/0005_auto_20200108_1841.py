# Generated by Django 2.2.6 on 2020-01-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tollapp', '0004_auto_20200106_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='Mode_of_payment',
            field=models.CharField(choices=[('Skrill', 'Skrill'), ('Neteller', 'Neteller'), ('Perfect money', 'Perfect money'), ('Bitcoin', 'Bitcoin'), ('Luno', 'Luno'), ('Bitpay', 'Bitpay')], max_length=100, null=True),
        ),
    ]
