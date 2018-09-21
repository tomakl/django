from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from .forms import CompetitorForm
from .models import Competition, Regulatory, Competitor
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


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


def competitor_list(request,pk):
    lists = Competitor.objects.get(pk=Competition.id)
    return render_to_response('register/list.html', {"lists": lists}, context_instance=RequestContext(request))

# Create your views here.
