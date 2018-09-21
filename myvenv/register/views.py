from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic import TemplateView
from .forms import CompetitorForm
from .models import Competition, Regulatory, Competitor
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger


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
    else:
        form = CompetitorForm(initial={'comp_name': event})
    return render(request, 'register/add.html', {'event': event, 'form': form})


def competitor_list(request, pk):
    lists = get_object_or_404(Competitor, pk=pk)
    paginator = Paginator(competitor_list, 5)
    page = request.GET.get('page')

    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    return render_to_response(request, 'register/list.html', {'lists': lists})

# Create your views here.
