from django.shortcuts import render_to_response, render
from models import Patient, HCR20
from panss.models import PANSS
from forms import PatientForm, HCR20Form
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from formtools.wizard.views import SessionWizardView
from django.template import RequestContext
from django.contrib.auth.models import User
# Create your views here.

#Shows List of Patients
@login_required
def patients(request):
    return render(request, 'patients.html',
                  {'patients': Patient.objects.all() })

#Shows individual patients - w/ details and ratings
@login_required
def patient(request, patient_id=1):
    return render(request, 'patient.html',
        {'patient': Patient.objects.get(id=patient_id),})

#create new patient - loads create patient Form
@login_required
def create(request):
    if request.POST:
        form = PatientForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.rating_date = timezone.now()
            c.created_by_id = request.user.id
            c.save()

            return HttpResponseRedirect('/patient/all/')

    else:
        form = PatientForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form


    return render(request, 'create_patient.html', args)


#creates new HCR20 rating
@login_required
def hcr20Form(request, patient_id):
    a = Patient.objects.get(id=patient_id)

    if request.method == "POST":
        f = HCR20Form(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.rating_date = timezone.now()
            c.created_by_id = request.user.id

            c.patient = a
            c.save()

            return HttpResponseRedirect('/patient/%s' % patient_id)
    else:
        f = HCR20Form()

    args = {}
    args.update(csrf(request))

    args['patient'] = a
    args['form'] = f

    return render(request, 'HCR20_form.html', args)


#Shows previous HCR20 ratings
@login_required
def hcr20(request, patient_id):

    return render(request, 'HCR20.html',{'hcr20': HCR20.objects.filter(patient__id=patient_id),
                                         'patient': Patient.objects.get(id=patient_id)})


