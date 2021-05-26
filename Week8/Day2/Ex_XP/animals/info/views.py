from django.shortcuts import render
from .models import Animal,Family

def animals(request):
    animals = Animal.objects.all()
    return render(request, 'all_animals.html', {'all_animals': animals})

def single_animal(request,animal_id):
    animal = Animal.objects.get(id=animal_id)
    print('hello')
    return render(request, 'single_animal.html', {'animal': animal})

# Create your views here.
