from django.urls import path
from . import views

urlpatterns = [
    path('person/name/<str:firstname>', views.person, name='person'),
    path('person/phonenumber/<str:phonenumber>', views.number),
    path('addperson',views.add_person, name='add_person'),
   
    ]