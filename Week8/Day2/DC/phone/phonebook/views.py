from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

# Create your views here.

def person(request, firstname ):
    person = Person.objects.get(first_name=firstname)
    print(person)
    return render(request, 'name.html', {'person': person})

def number(request, phonenumber ):
    person = Person.objects.get(phone_number=phonenumber)
    print(person)
    return render(request, 'phonenumber.html', {'person': person})

def add_person(request):
    if request.method == 'GET':
        return render(request, 'add_person.html', {'form': PersonForm})
    
    if request.method == 'POST':
        data = request.POST
        form = PersonForm(data)
        if form.is_valid():
            person = Person.objects.create(**form.cleaned_data)

            return redirect('person', person.first_name)
    