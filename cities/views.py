from django.shortcuts import render
from .models import City

__all__ = (
    'home',
)
def home(request):
    qs = City.objects.all()
    context = {'objects_list': qs}
    return render(request, 'city_home.html', context)
