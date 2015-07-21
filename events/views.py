from django.shortcuts import render
from models import Patient, Event
from forms import EventForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
@login_required
def eventForm(request, patient_id):
    a = Patient.objects.get(id=patient_id)

    if request.method == "POST":
        f = EventForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.created_by_id = request.user.id

            c.patient = a
            c.save()
            #takes user back to patient profile
            return HttpResponseRedirect('/patient/get/%s' % patient_id)
    else:
        f = EventForm()

    args = {}
    args.update(csrf(request))

    args['patient'] = a
    args['form'] = f

    return render(request, 'event_form.html', args)


@login_required
def event(request, patient_id):

    return render(request, 'event.html',{'event': Event.objects.filter(patient__id=patient_id),
                                         'patient': Patient.objects.get(id=patient_id),
                                         })
