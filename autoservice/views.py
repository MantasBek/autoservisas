from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Paslauga, Uzsakymas, Automobilis, Automobilio_modelis, Uzsakymo_eilute


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
    paginator = Paginator(Automobilis.objects.all(), 2)
    page_number = request.GET.get('page')
    automobiliai = paginator.get_page(page_number)
    context = {
        'automobiliai': automobiliai
    }
    return render(request, 'automobiliai.html', context=context)


def automobilis(request, automobilis_id):
    automobilis = get_object_or_404(Automobilis, pk=automobilis_id)
    return render(request, 'automobilis.html', {'automobilis': automobilis})


def search(request):
    query = request.GET.get('query')
    search_results = Automobilis.objects.filter(
        Q(vin_kodas__icontains=query) | Q(valstybinis_nr__icontains=query) | Q(klientas__icontains=query))
    search_results_2 = Automobilio_modelis.objects.filter(Q(marke__icontains=query) | Q(modelis__icontains=query))
    context = {
        'automobiliai': search_results,
        'automobilio_modelis': search_results_2,
        'query': query,
    }
    return render(request, 'search.html', context)


class UzsakymaiListView(generic.ListView):
    model = Uzsakymas
    paginate_by = 2
    template_name = 'uzsakymu_sarasas.html'


class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymo_eilute
    template_name = 'uzsakymas.html'


