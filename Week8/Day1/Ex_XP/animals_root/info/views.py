from django.shortcuts import render
from .templates.info import families,animals



def family(request, fam_id):
    for family in families:
        if family['id'] == fam_id:
            fam = family
            break

    
    return render(request,family.html, context={'fam': fam})

def animal(request, animal_id):
    data = read_json()
    return render(request, 'temolates/animal.html', context={})


