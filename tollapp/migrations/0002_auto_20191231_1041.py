# Generated by Django 2.2.6 on 2019-12-31 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tollapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='Mode_of_payment',
            field=models.CharField(choices=[('Card', 'Card'), ('Paypal', 'Paypal'), ('Skrill', 'Skrill'), ('Neteller', 'Neteller'), ('Perfect money', 'Perfect money'), ('Bitcoin', 'Bitcoin'), ('Luno', 'Luno'), ('Bitpay', 'Bitpay')], max_length=100, null=True),
        ),
    ]