from django.shortcuts import render, redirect
from .models import Family,Animal
from .forms import AnimalForm, FamilyForm

def all_animals(request):
    animals = Animal.objects.all()
    return render(request, 'all_animals.html', {'all_animals': animals})

def single_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'single_animal.html',{'animal': animal})

def single_family(request, family_id):
    fam = Family.objects.get(id=family_id)
    animals = fam.animal_set.all()
    return render(request, 'single_family.html', {'family': fam, 'animals': animals})

def add_animal(request):
    if request.method == 'GET':
        return render(request, 'add_animal.html',
         {'form': AnimalForm(), 'add_type':'Animal'})

    if request.method == 'POST':
        data = request.POST
        form = AnimalForm(data)
        if form.is_valid():
            print(form.cleaned_data)
            animal = Animal.objects.create(**form.cleaned_data)

        return redirect('all_animals')


def add_family(request):
    if request.method == 'GET':
        form = FamilyForm()
        return render(request, 'add_animal.html', {'form':form, 'add_type':'Family'})

    if request.method == 'POST':
        form = FamilyForm(request.POST)

        if form.is_valid():
            fam = Family.objects.create(name=form.cleaned_data['name'])

            return redirect ('single_family', fam.id)