# Generated by Django 2.2.6 on 2020-01-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tollapp', '0002_auto_20191231_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='Mode_of_payment',
            field=models.CharField(choices=[('Paypal', 'Paypal'), ('Skrill', 'Skrill'), ('Neteller', 'Neteller'), ('Perfect money', 'Perfect money'), ('Bitcoin', 'Bitcoin'), ('Luno', 'Luno'), ('Bitpay', 'Bitpay')], max_length=100, null=True),
        ),
    ]