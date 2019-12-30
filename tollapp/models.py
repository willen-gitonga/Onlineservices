from django.db import models
from django.contrib.auth.models import User

class Billing(models.Model):
    PAY_CHOICES = [
        ('Paypal', 'Paypal'),
        ('Skrill', 'Skrill'),
        ('Neteller', 'Neteller'),
        ('PerfectMoney', 'Perfect Money'),
        ('Bitcoin', 'Bitcoin'),
        ('Luno','Luno'),
        ('Bitpay','Bitpay'),    
    ]
    First_name = models.CharField(max_length =40)
    Last_name = models.CharField(max_length =40)
    Country = models.CharField(max_length =40)
    House_number_and_street_name = models.CharField(max_length =100)
    Town_or_City = models.CharField(max_length =100)
    State_or_Country = models.CharField(max_length =100)
    Postcode_or_ZIP = models.CharField(max_length =100)
    Phone = models.CharField(max_length =100)
    Email_address = models.CharField(max_length =100)
    Mode_of_payment = models.CharField(max_length =100,choices=PAY_CHOICES, null=True)

    def __str__(self):
        name = self.Email_address  
        return name




