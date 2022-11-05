from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from .forms import CityForm
from .models import City

__all__ = (
    'home', 'CityDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView','CityListView'
)


def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    # if pk:
    #     city = City.objects.filter(id=pk).first
    #     # city = get_object_or_404(City, id=pk)
    #     context = {'objects': city}
    #     return render(request, 'detail.html', context)

    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    form_class = CityForm
    template_name = 'detail.html'
    success_url = reverse_lazy('cities:home')


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'create.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно создан"


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'update.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно отредактирован"


class CityDeleteView(DeleteView):
    model = City
    template_name = 'delete.html'
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Город усешно удален')
        return self.post(request, *args, **kwargs)


class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context

