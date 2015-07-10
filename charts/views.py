from django.shortcuts import render, render_to_response
from rating.models import Patient, PANSS
from chartit import DataPool, Chart

# Create your views here.
def chartView(request, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve.
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': PANSS.objects.filter(patient__id=patient_id)},
              'terms': [
                'patient_id',
                'Q1',
                'Q2',
                'Q3',
                'Q4',
                'Q5',
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
                    'Q1',
                    'Q2',
                    'Q3',
                    'Q4',
                    'Q5'
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


