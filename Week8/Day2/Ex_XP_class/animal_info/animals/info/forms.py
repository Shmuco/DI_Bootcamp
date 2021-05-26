from django import forms
from.models import Family

class AnimalForm(forms.Form):
    name = forms.CharField(max_length=40)
    legs = forms.IntegerField()
    weight = forms.FloatField()
    height = forms.FloatField()
    speed = forms.FloatField()
    family = forms.ModelChoiceField(queryset=Family.objects.all())

class FamilyForm(forms.Form):
    name = forms.CharField(max_length=40)