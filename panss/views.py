from django.shortcuts import render
from models import PANSS, FullPANSS
from rating.models import Patient
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from forms import PANSSForm, PANSSFormFull
from django.template import RequestContext

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
    a = Patient.objects.get(id=patient_id)

    if request.method == "POST":
        f = PANSSForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.rating_date = timezone.now()
            c.created_by_id = request.user.id
            c.patient = a
            c.save()
            #takes user back to patient panss screen
            return HttpResponseRedirect('/patient/panss/%s' % patient_id)
    else:
        f = PANSSForm()

    args = {}
    args.update(csrf(request))

    args['patient'] = a
    args['form'] = f

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