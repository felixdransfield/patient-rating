__author__ = 'felixdransfield'

from django import forms
from django.forms.models import ModelForm, ModelFormMetaclass
from models import Patient, Update, PANSS, HCR20
from django.utils.safestring import mark_safe

#THe Patient form for creating a new patient - with the basic info
class PatientForm(forms.ModelForm):


    class Meta:
        model = Patient
        fields = ('name','hospital_id', 'DOB', 'DOA', 'DOD')




#rating choices are used for Panns and HCR20 - they are used to give subjective ratings for each field in the forms.
#they are used in ChoiceField(choice...)
rating_choices = (
        (1, 'Better'),
        (0, 'Same'),
        (-1, 'Worse'),

    )

#Renders the Radioselect buttons horizontally (for speed in filling in  forms)
class HorizontalRadioRenderer(forms.RadioSelect.renderer):

    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


#The PANSS form for adding a PANSS update to a patient, Gives each question a radioselect button with rating_choices arguments
class PANSSForm(forms.ModelForm):


    class Meta:
        model = PANSS
        fields = ('P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'G1', 'G2', 'G3', 'G4',
                    'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'S1', 'S2', 'S3')
        widgets = {
            'P1': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'P2': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'P3': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'P4': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'P5': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'P6': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'P7': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'N1': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'N2': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'N3': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'N4': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'N5': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'N6': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'N7': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G1': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G2': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G3': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G4': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G5': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G6': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G7': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G8': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G9': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G10': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G11': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G12': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G13': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G14': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G15': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'G16': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'S1': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'S2': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),
            'S3': forms.RadioSelect(choices=rating_choices,  renderer=HorizontalRadioRenderer),

        }




#The PANSS form for adding a PANSS update to a patient, Gives each question a radioselect button whit rating_choices arguments
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




#Depreceated
class UpdateForm(forms.ModelForm):

    class Meta:
        model = Update
        fields = ('rating_1', 'rating_2')