from django import forms
from .models import Category,Gifs


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=40)

class GifsForm(forms.Form):
    title = forms.CharField(max_length=40)
    url = forms.URLField()
    uploader_name = forms.CharField(max_length=40)
    category = forms.ModelMultipleChoiceField(queryset = Category.objects.all())
