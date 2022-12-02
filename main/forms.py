from django import forms
from django.forms import TextInput, DateTimeInput, NumberInput
from .models import SaveConcreate


class CreateConcreteForms(forms.ModelForm):
    class Meta:
        model = SaveConcreate
        fields = ['data', 'factory_name', 'object_name',
                  'block', 'mark', 'constructive', 'floor', 'fact_concrete',
                  'sum_concrete', 'accepted']

        widgets = {
            'data': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата'}),
            'factory_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название завода'}),
            'object_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название объекта'}),
            'block': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Блок'}),
            'mark': TextInput(attrs={'class': 'form-control', 'placeholder': 'Марка бетона'}),
            'constructive': TextInput(attrs={'class': 'form-control', 'placeholder': 'Конструктив'}),
            'floor': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Этаж'}),
            'fact_concrete': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Факт'}),
            'sum_concrete': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Итого залито'}),
            'accepted': TextInput(attrs={'class': 'form-control', 'placeholder': 'Кто принимал'}),
        }
