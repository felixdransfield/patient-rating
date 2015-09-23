from django.shortcuts import render
from models import PANSS, FullPANSS, PANSSFilter
from rating.models import Patient
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from forms import PANSSForm, PANSSFormFull, PANSSFilterForm
from chartit import DataPool, Chart
from charts.views import TargetsChart


#Shows Panss ratings for specific patient - based on context
@login_required
def panss(request, patient_id):
    a = FullPANSS.objects.filter(patient__id=patient_id, is_admission=True)
    group_id = request.user.groups.get().id
    if a.exists():
        return render(request, 'panss.html',{'panss': PANSS.objects.filter(patient__id=patient_id),
                                         'patient': Patient.objects.get(id=patient_id),
                                         'has_admission': True,
                                         'group_id': group_id,
                                         'fullpanss': FullPANSS.objects.get(patient__id=patient_id, is_current=True),
                                         })
    else:
        return render(request, 'panss.html',{'panss': PANSS.objects.filter(patient__id=patient_id),
                                        'patient': Patient.objects.get(id=patient_id),
                                         'has_admission': False,
                                         })


@login_required
def panssItem(request, panss_id, patient_id):

    return render(request, 'panssItem.html',{'panssItem': PANSS.objects.filter(patient__id=patient_id, id=panss_id),
                                         'patient': Patient.objects.get(id=patient_id),
                                         })



#creates a new Panss rating - using Panss Form
@login_required
def panssForm(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    existing_filter = PANSSFilter.objects.get(patient__id=patient_id, is_current=True)

    fields = {}

    if existing_filter.P1 == True:
        fields['P1'] = 'P1'




    if request.method == "POST":
        f = PANSSForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.rating_date = timezone.now()
            c.created_by_id = request.user.id
            c.patient = patient
            c.save()
            #takes user back to patient panss screen
            return HttpResponseRedirect('/patient/panss/%s' % patient_id)
    else:
        f = PANSSForm()

    args = {}
    args.update(csrf(request))
    args['patient'] = patient
    args['form'] = f
    args['existing_filter'] = existing_filter
    args['fields'] = fields



    return render(request, 'panss_form.html', args)


@login_required
def panssFormFull(request, patient_id):
    a = Patient.objects.get(id=patient_id)
    b = FullPANSS.objects.filter(patient__id=patient_id, is_admission=True)
    e = FullPANSS.objects.filter(patient__id=patient_id, is_admission=False, is_current=True)

    if request.method == "POST":
        f = PANSSFormFull(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.rating_date = timezone.now()
            c.created_by_id = request.user.id
            if b.exists():
                if e.exists():
                    d = FullPANSS.objects.get(patient__id=patient_id, is_admission=True)
                    e = FullPANSS.objects.get(patient__id=patient_id, is_admission=False, is_current=True)
                    c.is_admission = False
                    c.is_current = True
                    c.is_discharge = False
                    d.is_current = False
                    d.save()
                    e.is_current = False
                    e.save()
                else:
                    d = FullPANSS.objects.get(patient__id=patient_id, is_admission=True)
                    c.is_admission = False
                    c.is_current = True
                    c.is_discharge = False
                    d.is_current = False
                    d.save()

            else:
                c.is_admission = True
                c.is_current = True
                c.is_discharge = False
            c.patient = a
            c.save()
            #takes user back to patient panss screen
            return HttpResponseRedirect('/patient/panss/%s' % patient_id)
    else:
        f = PANSSFormFull()

    args = {}
    args.update(csrf(request))
    args['patient'] = a
    args['form'] = f

    return render(request, 'panss_form_full.html', args)

@login_required
def panssTargets(request, patient_id, fullpanss_id):
    patient = Patient.objects.get(id=patient_id)
    filter = PANSSFilter._meta.get_fields()

    ds = \
        DataPool(
           series=
            [{'options': {
                'source': FullPANSS.objects.filter(patient__id=patient_id, id=fullpanss_id, is_current=True),


            },
              'terms': [
                'P1','P2','P3','P4','P5','P6','P7',
                'N1','N2','N3','N4','N5','N6','N7',
                'G1','G2','G3','G4','G5','G6','G7','G8','G9','G10','G11','G12','G13','G14','G15','G16',
                'S1','S2','S3',
                'id'
                ]},




        ])

#Step 2: declares the variables for the chart
    cht = Chart(
            datasource = ds,
            series_options =
              [{'options':{
                  'type': 'column',
                  'pointWidth': 20,
                  'index':[ 'P1','P2','P3','P4','P5','P6','P7','N1','N2','N3','N4','N5','N6','N7','G1','G2','G3','G4','G5','G6','G7','G8','G9','G10','G11','G12','G13','G14','G15','G16','S1','S2','S3',],

                  },
                'terms':{
                  'id': [
                    'P1','P2','P3','P4','P5','P6','P7',
                    'N1','N2','N3','N4','N5','N6','N7',
                    'G1','G2','G3','G4','G5','G6','G7','G8','G9','G10','G11','G12','G13','G14','G15','G16',
                    'S1','S2','S3',
                        ]
                  }}],
            chart_options=
                {'chart': {
                    'height': 1000,
                    'inverted': True,
                     # 'margin': [0, 0, 0, 0],
                     # 'spacing': [0, 0, 0, 0],
                    },
                    'title': {'text': 'Set Rating Targets for %s' % patient.name },
                    'xAxis': {
                        'categories': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                    },
                    'yAxis': {
                        'title': {'text': 'Score'},
                        'tickInterval': 1

                    },
                    'credits': {'enabled': False },
                })

    existingFilter = PANSSFilter.objects.filter(patient_id=patient_id)

    f = PANSSFilterForm(request.POST)
    if request.method == "POST":

            if f.is_valid:
                c = f.save(commit=False)
                if existingFilter.exists():
                    a = PANSSFilter.objects.get(patient_id=patient_id, is_current=True)
                    a.is_current = False
                    a.save()
                    c.is_current = True
                    c.patient = patient
                    c.save()
                    return HttpResponseRedirect('/patient/panss/%s' % patient_id)
                else:
                    c.is_current = True
                    c.patient = patient
                    c.save()
                    return HttpResponseRedirect('/patient/panss/%s' % patient_id)
            else:
                f = PANSSFormFull()


    args = {}

    args['ds'] = cht
    args['fullpanss'] = FullPANSS.objects.get(patient__id=patient_id, id=fullpanss_id)
    args['patient'] = Patient.objects.get(id=patient_id)
    args['filter'] = filter
    args['form'] = f

    return render(request, 'pansstest.html', args)




#trying to add pagination ############

# class PANSSWizard( SessionWizardView ):
#     template_name = 'panss_form1.html'
#
#     def dispatch(self, request, patient_id, *args, **kwargs):
#         self.instance_dict = {
#             '0': Patient.objects.get(id=patient_id)
#
#         }
#         return super(PANSSWizard, self).dispatch(request, *args, **kwargs)
#
#     def done( self, form_list, **kwargs ):
#         self.instance.save()
#####################################change urls back to panssForm