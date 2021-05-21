from django.urls import path
from . import views

urlpatterns = [
    path('compare-animal/', views.compare_animal, name='compare-animal'),
    path('compare-data-collect/', views.compare_data_collect, name='compare-data-collect'),
    path('compare-lowfatality/', views.index, name='compare-lowfatality'),
    path('compare-mers-sars/', views.compare_mers_sars, name='compare-mers-sars'),
    path('compare-visualization/', views.compare_visualization, name='compare-visualization'),
    path('covid-about/', views.covid_about, name='covid-about'),
    path('covid-data-collect/', views.covid_data_collect, name='covid-data-collect'),
    path('covid-result/', views.covid_result, name='covid-result'),
    path('covid-sequence-alignment/', views.covid_sequence_alignment, name='covid-sequence-alignment'),
    path('covid-visualization/', views.covid_visualization, name='covid-visualization'),
    path('index/', views.index, name='index'),
    path('intro-algorithm/', views.intro_algorithm, name='intro-algorithm'),
    path('intro-team/', views.intro_team, name='intro-team'),

]