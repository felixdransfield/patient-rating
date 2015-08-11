__author__ = 'felixdransfield'

from django import forms
from django.forms.models import ModelForm, ModelFormMetaclass
from models import Patient, Update, HCR20
from panss.models import PANSS
from django.utils.safestring import mark_safe

rating_choices = (
        (1, 'Better'),
        (0, 'Same'),
        (-1, 'Worse'),

    )

#Renders the Radioselect buttons horizontally (for speed in filling in  forms)
class HorizontalRadioRenderer(forms.RadioSelect.renderer):

    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

#THe Patient form for creating a new patient - with the basic info
class PatientForm(forms.ModelForm):


    class Meta:
        model = Patient
        fields = ('name','hospital_id', 'DOB', 'DOA', 'DOD')
        widgets = {
            'DOB': forms.DateInput(attrs={'type':'date'}),
            'DOA': forms.DateInput(attrs={'type':'date'}),
            'DOD': forms.DateInput(attrs={'type':'date'})
        }





#The HCR20 form for adding a PANSS HCR20 to a patient, Gives each question a radioselect button whit rating_choices arguments
class HCR20Form(forms.ModelForm):
    H1 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    H2 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    H3 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    H4 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    H5 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    H6 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    H7 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    H8 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    H9 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    H10 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    C1 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    C2 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    C3 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    C4 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    C5 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    R1 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    R2 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    R3 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    R4 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    R5 = forms.ChoiceField(choices=rating_choices,
                                 initial=0,
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))

    class Meta:
        model = HCR20
        fields = ('H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'C1', 'C2', 'C3', 'C4', 'C5', 'R1', 'R2', 'R3',
                    'R4', 'R5')
        widgets = {'fields': forms.RadioSelect}



