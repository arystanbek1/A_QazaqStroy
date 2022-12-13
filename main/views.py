from django.shortcuts import render, redirect
from .models import SaveConcrete, Registration, Object
from .forms import CreateConcreteForms, RegistrationForms
from django.views.generic import UpdateView, DeleteView, DetailView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers.serializer import ObjectSerializer


def regis(request):
    form = RegistrationForms
    error = ''
    data = {
        'form': form,
        'error': error,

    }
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        else:
            error = 'Не правильно заполнили'
    return render(request, 'main/registration.html', data)


def base(request):
    return render(request, 'main/base.html')


def table(request):
    model_concrete = SaveConcrete.objects.all()
    return render(request, 'main/table.html', {'model_concrete': model_concrete})


def create(request):
    form = CreateConcreteForms
    error = ''
    data = {
        'form': form,
        'error': error,
    }

    if request.method == 'POST':
        form = CreateConcreteForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/table')
        else:
            error = 'Не правильно заполнили'

    return render(request, 'main/create.html', data)


class ConcreteDetailView(DetailView):
    model = SaveConcrete
    template_name = 'main/detail.html'
    context_object_name = 'el'


class ConcreteUpdateView(UpdateView):
    model = SaveConcrete
    template_name = 'main/create.html'
    form_class = CreateConcreteForms


class ConcreteDeleteView(DeleteView):
    model = SaveConcrete
    success_url = 'http://127.0.0.1:8000/table'
    template_name = 'main/delete.html'


class ObjectViewSet(ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = [AllowAny, ]



