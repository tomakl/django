from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig, SingleTableMixin
from .forms import CompetitorForm
from .models import Competition, Regulatory, Competitor
from django.contrib import messages
from .tables import CompetitorTable
import django_filters


def competition_list(request):
    comps = Competition.objects.all().values('id', 'name', 'distance', 'date', 'price', 'reg_name', 'image', 'info',
                                             'place', 'allowed', 'reported', 'status')
    return render(request, 'register/compe_list.html', {'comps': comps})


def reg_detail(request, pk):
    detail = get_object_or_404(Regulatory, pk=pk)
    return render(request, 'register/reg_details.html', {'detail': detail})


def add(request, pk):
    event = get_object_or_404(Competition, pk=pk)
    if request.POST:
        form = CompetitorForm(request.POST)
        if form.is_valid():
            competitor = form.save(commit=False)
            competitor.comp_name = event
            competitor.save()
            messages.success(request, 'Twoje zgłoszenie zostało przyjęte')
    else:
        form = CompetitorForm(initial={'comp_name': event})

    return render(request, 'register/add.html', {'event': event, 'form': form})


def competitor_list(request, pk):

    lists = CompetitorTable(Competitor.objects.filter(comp_name_id=pk).all(), order_by = "start_number")
    RequestConfig(request, paginate={"per_page": 10}).configure(lists)
    return render(request, 'register/list.html', {'lists': lists})




# Create your views here.
