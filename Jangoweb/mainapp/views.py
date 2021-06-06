from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from mainapp.models import Sequence


def compare_animal(request):
    template = loader.get_template('compare-animal.html')
    return HttpResponse(template.render(None, request))

def compare_data_collect(request):
    template = loader.get_template('compare-data-collect.html')
    return HttpResponse(template.render(None, request))

def compare_lowfatality(request):
    template = loader.get_template('compare-lowfatality.html')
    return HttpResponse(template.render(None, request))

def compare_mers_sars(request):
    template = loader.get_template('compare-mers-sars.html')
    return HttpResponse(template.render(None, request))

def compare_visualization(request):
    template = loader.get_template('compare-visualization.html')
    return HttpResponse(template.render(None, request))

def covid_data_collect(request):
    template = loader.get_template('covid-data-collect.html')
    return HttpResponse(template.render(None, request))

def covid_result(request):
    template = loader.get_template('covid-result.html')
    return HttpResponse(template.render(None, request))

def covid_sequence_alignment(request):
    template = loader.get_template('covid-sequence-alignment.html')
    return HttpResponse(template.render(None, request))

def covid_visualization(request):
    template = loader.get_template('covid-visualization.html')
    return HttpResponse(template.render(None, request))

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(None, request))

def intro_algorithm(request):
    template = loader.get_template('intro-algorithm.html')
    return HttpResponse(template.render(None, request))

def intro_team(request):
    template = loader.get_template('intro-team.html')
    return HttpResponse(template.render(None, request))

@method_decorator(csrf_exempt,name='dispatch')
def execute(request):
    #template = loader.get_template('execute.html')
    # return HttpResponse(template.render(None, request))

    if request.method == "POST":
        name1 = request.POST.get('namecode1')
        name2 = request.POST.get('namecode2')

        sequence1 = Sequence()
        if name1 == sequence1.getNamecode():
            return render(request, 'execute.html', context={'text': name1})

    else:
        return render(request, 'execute.html')

# Create your views here.
