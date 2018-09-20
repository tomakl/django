from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, render_to_response
from django.utils import timezone
from .models import Competition, Regulatory, Competitor
from datetime import datetime
from django.core.paginator import Paginator
from .forms import CompetitorForm
from django.contrib.auth import login, authenticate

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

def competition_list(request):
    comps = Competition.objects.all().values('id','name','distance','date','price','reg_name','image','info','place','allowed','reported','status')
    return render(request, 'register/compe_list.html', {'comps': comps})
    paginator = Paginator(comps, 2)

def reg_detail (request, pk):
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
        form = CompetitorForm(initial={'comp_name':event})

    return render(request, 'register/add.html', {'event': event, 'form': form})

def people(request):
    run = Competitor.objects.all().values('firstame', 'lastname',)
    return render(request, 'register/list.html', {'run': run})














# Create your views here.
