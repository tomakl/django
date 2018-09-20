from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
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
            ### NO NEED FOR - already set as part of valid modelform ::: rating = form.cleaned_data['rating']
            ### AS WELL AS ::: comment = form.cleaned_data['comment']

            ### THIS IS NOT A FIELD IN YOUR FORM :::user_name = form.cleaned_data['user_name']
            # compettitor = request.user.username

            competitor = form.save(commit=False) # commit = False means that this instantiate but not save a Review model object
            competitor.comp_name = event
            # competition.name = competition

            competitor.save() # save to the DB now
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('competitor:event', args=(competitor.id,))) # THIS will redirect only upon form save
    else:
        form = CompetitorForm(initial={'comp_name':event})


    return render(request, 'register/add.html', {'event': event, 'form': form})














# Create your views here.
