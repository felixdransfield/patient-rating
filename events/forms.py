__author__ = 'felixdransfield'

from django import forms
from django.forms.models import ModelForm, ModelFormMetaclass
from models import Patient, Event
from django.utils.safestring import mark_safe

class EventForm(forms.ModelForm):


    class Meta:
        model = Event
        fields = ('DOE',)
        widgets = {
            'DOE': forms.DateInput(attrs={'type':'date'}),

        }

