from django.shortcuts import render, render_to_response
from rating.models import Patient, PANSS
from chartit import DataPool, Chart

# Create your views here.
def Pchart(request, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve.
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': PANSS.objects.filter(patient__id=patient_id)},
              'terms': [
                'patient_id',
                'P1',
                'P2',
                'P3',
                'P4',
                'P5',
                'P6',
                'P7',
                'N1',
                'N2',
                'N3',
                'N4',
                'N5',
                'N6',
                'N7',
                'G1',
                'G2',
                'G3',
                'G4',
                'G5',
                'G6',
                'G7',
                'G8',
                'G9',
                'G10',
                'G11',
                'G12',
                'G13',
                'G14',
                'G15',
                'G16',
                'S1',
                'S2',
                'S3',
                'id',]}
             ])


    cht = Chart(
            datasource = ds,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'id': [
                    'P1',
                    'P2',
                    'P3',
                    'P4',
                    'P5',
                    'P6',
                    'P7',
                        ]
                  }}],
            chart_options =
              {'title': {
                   'text': 'PANSS scores for %s' % patient_id},
               'xAxis': {
                    'title': {
                       'text': 'Rating'}},
                'yAxis' : {
                  'title':{
                      'text': 'Score'
                  }
              }
              })


    #Step 3: Send the chart object to the template.
    return render_to_response('chart.html', {'ds':cht})

def Nchart(request, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve.
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': PANSS.objects.filter(patient__id=patient_id)},
              'terms': [
                'patient_id',
                'P1',
                'P2',
                'P3',
                'P4',
                'P5',
                'P6',
                'P7',
                'N1',
                'N2',
                'N3',
                'N4',
                'N5',
                'N6',
                'N7',
                'G1',
                'G2',
                'G3',
                'G4',
                'G5',
                'G6',
                'G7',
                'G8',
                'G9',
                'G10',
                'G11',
                'G12',
                'G13',
                'G14',
                'G15',
                'G16',
                'S1',
                'S2',
                'S3',
                'id',]}
             ])


    cht = Chart(
            datasource = ds,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'id': [
                    'N1',
                    'N2',
                    'N3',
                    'N4',
                    'N5',
                    'N6',
                    'N7',
                        ]
                  }}],
            chart_options =
              {'title': {
                   'text': 'PANSS scores for %s' % patient_id},
               'xAxis': {
                    'title': {
                       'text': 'Rating'}},
                'yAxis' : {
                  'title':{
                      'text': 'Score'
                  }
              }
              })


    #Step 3: Send the chart object to the template.
    return render_to_response('chart.html', {'ds':cht})

def Gchart(request, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve.
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': PANSS.objects.filter(patient__id=patient_id)},
              'terms': [
                'patient_id',
                'P1',
                'P2',
                'P3',
                'P4',
                'P5',
                'P6',
                'P7',
                'N1',
                'N2',
                'N3',
                'N4',
                'N5',
                'N6',
                'N7',
                'G1',
                'G2',
                'G3',
                'G4',
                'G5',
                'G6',
                'G7',
                'G8',
                'G9',
                'G10',
                'G11',
                'G12',
                'G13',
                'G14',
                'G15',
                'G16',
                'S1',
                'S2',
                'S3',
                'id',]}
             ])


    cht = Chart(
            datasource = ds,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'id': [
                    'G1',
                    'G2',
                    'G3',
                    'G4',
                    'G5',
                    'G6',
                    'G7',
                    'G8',
                    'G9',
                    'G10',
                    'G11',
                    'G12',
                    'G13',
                    'G14',
                    'G15',
                    'G16',
                        ]
                  }}],
            chart_options =
              {'title': {
                   'text': 'PANSS scores for %s' % patient_id},
               'xAxis': {
                    'title': {
                       'text': 'Rating'}},
                'yAxis' : {
                  'title':{
                      'text': 'Score'
                  }
              }
              })


    #Step 3: Send the chart object to the template.
    return render_to_response('chart.html', {'ds':cht})

def Schart(request, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve.
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': PANSS.objects.filter(patient__id=patient_id)},
              'terms': [
                'patient_id',
                'P1',
                'P2',
                'P3',
                'P4',
                'P5',
                'P6',
                'P7',
                'N1',
                'N2',
                'N3',
                'N4',
                'N5',
                'N6',
                'N7',
                'G1',
                'G2',
                'G3',
                'G4',
                'G5',
                'G6',
                'G7',
                'G8',
                'G9',
                'G10',
                'G11',
                'G12',
                'G13',
                'G14',
                'G15',
                'G16',
                'S1',
                'S2',
                'S3',
                'id',]}
             ])


    cht = Chart(
            datasource = ds,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'id': [
                    'S1',
                    'S2',
                    'S3',
                        ]
                  }}],
            chart_options =
              {'title': {
                   'text': 'PANSS scores for %s' % patient_id},
               'xAxis': {
                    'title': {
                       'text': 'Rating'}},
                'yAxis' : {
                  'title':{
                      'text': 'Score'
                  }
              }
              })


    #Step 3: Send the chart object to the template.
    return render_to_response('chart.html', {'ds':cht})
