from django.urls import path
from . import views

urlpatterns = [
    path('persons/<int:person_id>', views.phone_numer, name='phone_number'),
    
]