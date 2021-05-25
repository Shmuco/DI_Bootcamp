from django import forms
from  .models import Person
from phonenumber_field.modelfields import PhoneNumberField

class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    phone_number = PhoneNumberField()
    address = forms.CharField(max_length=100)