from django.shortcuts import render_to_response, render
from models import Patient, Update, PANSS, HCR20
from forms import PatientForm, UpdateForm, PANSSForm, HCR20Form
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.

#Shows List of Patients
@login_required
def patients(request):
    return render_to_response('patients.html',
                  {'patients': Patient.objects.all() })

#Shows individual patients - w/ details and ratings
@login_required
def patient(request, patient_id=1):
    return render_to_response('patient.html',
        {'patient': Patient.objects.get(id=patient_id)})

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


    return render_to_response('create_patient.html', args)


#Shows Panss ratings for specific patient - based on context
@login_required
def panss(request, patient_id):

    return render(request, 'panss.html',{'panss': PANSS.objects.filter(patient__id=patient_id)})


#creates a new Panss rating - using Panss Form
@login_required
def panssForm(request, patient_id):
    a = Patient.objects.get(id=patient_id)

    if request.method == "POST":
        f = PANSSForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.rating_date = timezone.now()
            c.created_by_id = request.user.id

            c.patient = a
            c.save()
            #takes user back to patient profile
            return HttpResponseRedirect('/patient/get/%s' % patient_id)
    else:
        f = PANSSForm()

    args = {}
    args.update(csrf(request))

    args['patient'] = a
    args['form'] = f

    return render_to_response('panss_form.html', args)

#creates ne HCR20 rating
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

            return HttpResponseRedirect('/patient/get/%s' % patient_id)
    else:
        f = HCR20Form()

    args = {}
    args.update(csrf(request))

    args['patient'] = a
    args['form'] = f

    return render_to_response('HCR20_form.html', args)


#Shows previous HCR20 ratings
@login_required
def hcr20(request, patient_id):

    return render(request, 'HCR20.html',{'hcr20': HCR20.objects.filter(patient__id=patient_id)})


#depreceated
@login_required
def update_patient(request, patient_id):
    a = Patient.objects.get(id=patient_id)

    if request.method == "POST":
        f = UpdateForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.rating_date = timezone.now()
            c.patient = a
            c.save()

            return HttpResponseRedirect('/patient/get/%s' % patient_id)

    else:
        f = UpdateForm()

    args = {}
    args.update(csrf(request))

    args['patient'] = a
    args['form'] = f

    return render_to_response('update_patient.html', args)