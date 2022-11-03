from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from .forms import HtmlForm, CityForm
from .models import City

__all__ = (
    'home','CityDetailView','CityCreateView',
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
    #     return render(request, 'city_detail.html', context)

    form = CityForm()
    qs = City.objects.all()
    context = {'objects_list': qs, 'form': form}
    return render(request, 'city_home.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'city_detail.html'

class CityCreateView(CreateView):
    queryset = City
    form_class = CityForm
    template_name = 'create.html'
    success_url = reverse_lazy('cities:home')