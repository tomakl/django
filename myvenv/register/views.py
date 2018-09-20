from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .forms import CompetitorForm
from .models import Competition, Regulatory, Competitor



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

def list(request,pk):
    run = get_object_or_404(Competition, pk=pk)
    return render(request, 'register/list.html', {'run': run})

class CompetitorView(TemplateView):
    template_name = 'register/users.html'

    def get_context_data(self,**kwargs):
        context = (CompetitorView,self).get_context_data(**kwargs)
        context['object_list'] = Competitor.objects.all()
        return context


# Create your views here.
