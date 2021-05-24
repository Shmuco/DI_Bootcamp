from django.shortcuts import render
from .models import Person

# Create your views here.

def phone_number(request, phone_number):
    person = Person.objects.get(id=person_id)
    return render(request, 'phonenumber.html', {'person': person})

def phone_number(request, first_name):
    person = Person.objects.get(id=person_id)
    return render(request, 'name.html', {'person': person})
