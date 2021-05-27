from django.urls import path
from . import views

urlpatterns = [
path('homepage/', views.homepage, name = 'homepage'),
path('addgif/', views.add_gif, name = 'addgif'),
path('addcat/', views.add_cat, name = 'addgcat'),
path('category/<int:category_id>', views.single_category, name = 'single_category'),
path('category/',views.all_categories, name= 'category' ),
path('gif/<int:gif_id>', views.single_gif, name = 'single_gif'),



]