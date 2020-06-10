from django import forms
from django.forms import ModelForm 
from . models import FormModel

class formNew(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = '__all__'