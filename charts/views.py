from django.shortcuts import render, render_to_response
from rating.models import Patient, HCR20
from panss.models import PANSS, FullPANSS
from chartit import DataPool, Chart




# Create your views here.

terms = ['patient_id','P1','P2','P3','P4','P5','P6','P7','N1','N2','N3','N4','N5','N6','N7','G1','G2','G3','G4','G5','G6','G7','G8','G9','G10','G11','G12','G13','G14','G15','G16','S1','S2','S3','id']

#Chart View for Positive subscale of PANSS
def Pchart(request, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve
    name =  Patient.objects.get(id=patient_id)
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': PANSS.objects.filter(patient__id=patient_id)},
              'terms': terms},

         ])

    #Step 2: declares the variables for the chart
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
                   'text': 'Positive Symptom scores for %s' % name},
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
    return render(request, 'chart.html', {'ds':cht, 'patient': Patient.objects.get(id=patient_id) })

#Chart View for Negative subscale of PANSS
def Nchart(request, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve.
    name =  Patient.objects.get(id=patient_id)
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': PANSS.objects.filter(patient__id=patient_id)},
              'terms': terms}
             ])

    #Step 2: declares the variables for the chart
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
                   'text': 'Negative Symptom scores for %s' % name},
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
    return render(request, 'chart.html', {'ds':cht, 'patient': Patient.objects.get(id=patient_id)})

#Chart View for General subscale of PANSS
def Gchart(request, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve.
    name =  Patient.objects.get(id=patient_id)
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': PANSS.objects.filter(patient__id=patient_id)},
              'terms': terms}
             ])

    #Step 2: declares the variables for the chart
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
                   'text': 'General Symptom scores for %s' % name},
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
    return render(request, 'chart.html', {'ds':cht, 'patient': Patient.objects.get(id=patient_id)})

#Chart View for Additonal Symptoms subscale of PANSS
def Schart(request, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve.
    name =  Patient.objects.get(id=patient_id)
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': PANSS.objects.filter(patient__id=patient_id)},
              'terms': terms}
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
                   'text': 'Additional Symptoms scores for %s' % name},
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
    return render(request, 'chart.html', {'ds':cht, 'patient': Patient.objects.get(id=patient_id)})

#Chart View for Historical subscale of HCR20
def Hchart(request, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve.
    name =  Patient.objects.get(id=patient_id)
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': HCR20.objects.filter(patient__id=patient_id)},
              'terms': [
                'patient_id',
                'H1',
                'H2',
                'H3',
                'H4',
                'H5',
                'H6',
                'H7',
                'H8',
                'H9',
                'H10',
                'C1',
                'C2',
                'C3',
                'C4',
                'C5',
                'R1',
                'R2',
                'R3',
                'R4',
                'R5',
                'id',]}
             ])

    #Step 2: declares the variables for the chart
    cht = Chart(
            datasource = ds,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'id': [
                    'H1',
                    'H2',
                    'H3',
                    'H4',
                    'H5',
                    'H6',
                    'H7',
                    'H8',
                    'H9',
                    'H10',
                        ]
                  }}],
            chart_options =
              {'title': {
                   'text': 'HCR20 Historical scores for %s' % name},
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
    return render(request, 'chart.html', {'ds':cht, 'patient': Patient.objects.get(id=patient_id)})

#Chart View for Clinical subscale of HCR20
def Cchart(request, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve.
    name =  Patient.objects.get(id=patient_id)
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': HCR20.objects.filter(patient__id=patient_id)},
              'terms': [
                'patient_id',
                'H1',
                'H2',
                'H3',
                'H4',
                'H5',
                'H6',
                'H7',
                'H8',
                'H9',
                'H10',
                'C1',
                'C2',
                'C3',
                'C4',
                'C5',
                'R1',
                'R2',
                'R3',
                'R4',
                'R5',
                'id',]}
             ])

    #Step 2: declares the variables for the chart
    cht = Chart(
            datasource = ds,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'id': [
                    'C1',
                    'C2',
                    'C3',
                    'C4',
                    'C5',
                        ]
                  }}],
            chart_options =
              {'title': {
                   'text': 'HCR20 Clinical scores for %s' % name},
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
    return render(request, 'chart.html', {'ds':cht, 'patient': Patient.objects.get(id=patient_id)})

#Chart View for Risk Management subscale of HCR20
def Rchart(request, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve.
    name =  Patient.objects.get(id=patient_id)
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': HCR20.objects.filter(patient__id=patient_id)},
              'terms': [
                'patient_id',
                'H1',
                'H2',
                'H3',
                'H4',
                'H5',
                'H6',
                'H7',
                'H8',
                'H9',
                'H10',
                'C1',
                'C2',
                'C3',
                'C4',
                'C5',
                'R1',
                'R2',
                'R3',
                'R4',
                'R5',
                'id',]}
             ])

    #Step 2: declares the variables for the chart
    cht = Chart(
            datasource = ds,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'id': [
                    'R1',
                    'R2',
                    'R3',
                    'R4',
                    'R5',
                        ]
                  }}],
            chart_options =
              {'title': {
                   'text': 'HCR20 Risk Management scores for %s' % name},
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
    return render(request, 'chart.html', {'ds':cht, 'patient': Patient.objects.get(id=patient_id)})

def PanssItemChart(request, panss_id, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve
    name =  Patient.objects.get(id=patient_id)
    ds = \
        DataPool(
           series=
            [{'options': {
               'source': PANSS.objects.filter(patient__id=patient_id, id=panss_id)},
              'terms': [
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
                'id',]},

         ])

    #Step 2: declares the variables for the chart
    cht = Chart(
            datasource = ds,
            series_options =
              [{'options':{
                  'type': 'column',
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
                   'text': 'Positive Symptom scores for %s' % name},
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
    return render(request, 'panssItem.html', {'ds':cht, 'panssItem': PANSS.objects.filter(patient__id=patient_id, id=panss_id),
                                         'patient': Patient.objects.get(id=patient_id),

                                         })


def TargetsChart(cht, fullpanss_id, patient_id):
    #Step 1: Create a DataPool with the data we want to retrieve

    ds = \
        DataPool(
           series=
            [{'options': {
               'source': FullPANSS.objects.filter(patient__id=patient_id, id=fullpanss_id, is_current=True)},
              'terms': [
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
                'id',]},

         ])

    #Step 2: declares the variables for the chart
    cht = Chart(
            datasource = ds,
            series_options =
              [{'options':{
                  'type': 'column',
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
                        ]
                  }}],
            chart_options =
              {'title': {
                   'text': 'Set Rating Targets' },
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
    return cht
