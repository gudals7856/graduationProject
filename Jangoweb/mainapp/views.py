from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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


# Create your views here.
