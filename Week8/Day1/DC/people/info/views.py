from django.shortcuts import render
from .data import people 
# Create your views here.

def peo(request):
    p = 'hello'
    return render(request,'people.html', context= {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  })

 


