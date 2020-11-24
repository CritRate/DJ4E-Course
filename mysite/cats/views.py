from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

from .models import Cat, Breed


def home(request):
    return HttpResponse('Hello')


class BreedList(ListView):
    model = Breed
    paginate_by = 100


class BreedUpdate(UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedCreate(CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedDelete(DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:all')


class CatList(ListView):
    model = Cat
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breed_count'] = Breed.objects.all().count()
        return context


class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:all')
