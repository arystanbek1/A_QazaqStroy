from django import forms
from django.forms import TextInput, DateTimeInput, NumberInput
from .models import SaveConcrete, Registration
from .choice import FactoryChoice, ConstructiveChoice, CustomUserRoleChoice, MarkConcreteChoice


class CreateConcreteForms(forms.ModelForm):
    class Meta:
        model = SaveConcrete
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


# class CreateConcreteForms(forms.Form):
#     model = SaveConcrete
#     data = forms.DateField(label='Дата')
#     factory_name = forms.ChoiceField(label='Завод', choices=FactoryChoice.choices)
#     object_name = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название объекта'}),
#     block = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Блок'}),
#     mark = forms.ChoiceField(label='Марка', choices=MarkConcreteChoice.choices),
#     constructive = forms.ChoiceField(label='Конструктив', choices=ConstructiveChoice.choices),
#     floor = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Этаж'}),
#     fact_concrete = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Факт'}),
#     sum_concrete = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Итого залито'}),
#     accepted = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кто принимал'}),


class RegistrationForms(forms.ModelForm):
    class Meta:
        model = Registration

        fields = ['name', 'surname', 'phone', 'sms']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон номер'}),
            'sms': TextInput(attrs={'class': 'form-control', 'placeholder': 'СМС'}),
        }