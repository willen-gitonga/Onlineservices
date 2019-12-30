from django import forms
from django.forms import ModelForm, Textarea, IntegerField


from .models import Billing

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        exclude = ['user']