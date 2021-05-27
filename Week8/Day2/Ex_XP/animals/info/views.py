from django.shortcuts import render
from .models import Animal,Family

# not printing on HTML
def all_animals(request):
    all_animals = Animal.objects.all()
    for i in all_animals:
        print(i.name)
    return render(request, 'all_animals.html', {'all_animals':all_animals})

def single_animal(request,animal_id):
    animal = Animal.objects.get(id=animal_id)
    print('hello')
    return render(request, 'single_animal.html', {'animal': animal})

def single_family(request,family_id):
    print('hello')
    family = Animal.objects.filter(family=family_id)
    return render(request, 'single_family.html', {'family':family})
