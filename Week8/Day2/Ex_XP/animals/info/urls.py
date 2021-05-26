from django.urls import path
from . import views


urlpatterns = [
    path('animals/', views.animals, name='animals'),
    path('animal/<int:animal_id>', views.single_animal, name='single_animals'),
    
    # path('animal/<int:animal_id>', views.animal_id, name='animal_id'),
    # path('family/<int:family_id>', views.family_id, name = 'family_id'),
]