from django.shortcuts import render, get_object_or_404
from .models import Paslauga, Uzsakymas, Automobilis

def index(request):
    services_count = Paslauga.objects.count()
    orders_count = Uzsakymas.objects.count()
    cars_count = Automobilis.objects.count()

    context = {
        'services_count': services_count,
        'orders_count': orders_count,
        'cars_count': cars_count,
    }

    return render(request, 'index.html', context)

def automobiliai(request):
    automobiliai = Automobilis.objects.all()
    context = {
        'automobiliai': automobiliai
    }
    return render(request, 'automobiliai.html', context=context)

def automobilis(request, automobilis_id):
    automobilis = get_object_or_404(Automobilis, pk=automobilis_id)
    return render(request, 'automobilis.html', {'automobilis': automobilis})