# Generated by Django 2.2.6 on 2019-12-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tollapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=40)),
                ('Last_name', models.CharField(max_length=40)),
                ('Country', models.CharField(max_length=40)),
                ('House_number_and_street_name', models.CharField(max_length=100)),
                ('Town_or_City', models.CharField(max_length=100)),
                ('State_or_Country', models.CharField(max_length=100)),
                ('Postcode_or_ZIP', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=100)),
                ('Email_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Bursary',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Future_plans',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
