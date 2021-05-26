from django.shortcuts import render, redirect
from .models import Gifs,Category
from .forms import CategoryForm, GifsForm

# Create your views here.

def homepage(request):
    gifs = Gifs.objects.all()
    
    return render(request,'homepage.html', {'gifs':gifs})

def add_gif(request):
    print('worlo')
    if request.method == 'GET':
        return render (request, 'add_cat.html', {'form': GifsForm(), 'add_type': 'Gif'})

def add_cat(request):
    if request.method == 'GET':
        print(CategoryForm())
        print(GifsForm())
        return render(request, 'add_cat.html', {'form': CategoryForm(),'add_type': 'Category'})
    
    if request.method == 'POST':
        data = request.POST
        form = CategoryForm(data)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
    return redirect('homepage')

def single_category(request, category_id):
    category = Gifs.objects.filter(category=category_id)
    return render(request, 'single_category.html', {'gifs': category})

def category(request):
    categories = Category.objects.all()
    print(categories)
    return render(request,'all_categories.html', {'categories':categories})
    
def single_gif(request, gif_id):
    gif = Gifs.objects.get(id=gif_id)
    print(type(gif.category))
    return render(request, 'single_gif.html', {'gif': gif})
