__author__ = 'felixdransfield'

from django import forms
from django.forms.models import ModelForm, ModelFormMetaclass
from models import Patient, Event
from rating.forms import HorizontalRadioRenderer
from django.utils.safestring import mark_safe

event_choices = (
        ('1', 'Medication change'),
        ('2', 'Management plan change'),
        ('3', 'Other Stressor')
    )

class EventForm(forms.ModelForm):


    class Meta:
        model = Event
        fields = ('DOE', 'event_type', 'event_description')
        widgets = {
            'DOE': forms.DateInput(attrs={'type':'date'}),
            'event_type': forms.RadioSelect(choices=event_choices),

        }

