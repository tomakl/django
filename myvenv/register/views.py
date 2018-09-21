from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .forms import CompetitorForm
from .models import Competition, Regulatory, Competitor
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def competition_list(request):
    comps = Competition.objects.all().values('id', 'name', 'distance', 'date', 'price', 'reg_name', 'image', 'info',
                                             'place', 'allowed', 'reported', 'status')
    return render(request, 'register/compe_list.html', {'comps': comps})
    paginator = Paginator(comps, 2)


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
    page = request.GET.get('page', 1)
    paginator = Paginator(competitor_list, 1)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)
    return render(request, 'register/list.html', {'lists': lists})

# Create your views here.
