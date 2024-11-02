# forms.py
from django import forms
from .models import ProjectElement, Material

class QuotationRequestForm(forms.Form):
    element = forms.ModelChoiceField(queryset=ProjectElement.objects.all(), widget=forms.RadioSelect)
    material = forms.ModelChoiceField(queryset=Material.objects.all(), widget=forms.RadioSelect, required=False)
