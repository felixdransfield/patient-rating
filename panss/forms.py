from django import forms
from models import PANSS, FullPANSS
from rating.models import Patient
from django.utils.safestring import mark_safe

# rating choices are used for Panns and HCR20 - they are used to give subjective ratings for each field in the forms.
# they are used in ChoiceField(choice...)
rating_choices = (
    (1, 'Better'),
    (0, 'Same'),
    (-1, 'Worse'),

)

full_choices = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
)

#Renders the Radioselect buttons horizontally (for speed in filling in  forms)
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


#The PANSS form for adding a PANSS update to a patient, Gives each question a radioselect button with rating_choices arguments
class PANSSForm(forms.ModelForm):
    class Meta:
        model = PANSS
        fields = (
            'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'G1', 'G2', 'G3', 'G4',
            'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'S1', 'S2', 'S3')
        widgets = {
            'P1': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer, attrs={'autofocus': 'autofocus'}),
            'P2': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'P3': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'P4': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'P5': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'P6': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'P7': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N1': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N2': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N3': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N4': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N5': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N6': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N7': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G1': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G2': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G3': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G4': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G5': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G6': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G7': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G8': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G9': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G10': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G11': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G12': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G13': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G14': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G15': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G16': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'S1': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'S2': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'S3': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),

        }


class PANSSFormFull(forms.ModelForm):
    class Meta:
        model = FullPANSS
        fields = (
            'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'G1', 'G2', 'G3', 'G4',
            'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'S1', 'S2', 'S3')

        widgets = {
            'P1': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer,
                                    attrs={'autofocus': 'autofocus'}),
            'P2': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'P3': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'P4': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'P5': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'P6': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'P7': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'N1': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'N2': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'N3': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'N4': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'N5': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'N6': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'N7': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G1': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G2': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G3': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G4': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G5': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G6': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G7': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G8': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G9': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G10': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G11': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G12': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G13': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G14': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G15': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'G16': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'S1': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'S2': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),
            'S3': forms.RadioSelect(choices=full_choices, renderer=HorizontalRadioRenderer),

        }


#trying to paginate forms
class PANSSPositiveForm(forms.ModelForm):
    class Meta:
        model = PANSS
        fields = ('P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7')
        widgets = {
            'P1': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'P2': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'P3': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'P4': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'P5': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'P6': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'P7': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer)

        }


class PANSSNegativeForm(forms.ModelForm):
    class Meta:
        model = PANSS
        fields = ('N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7')
        widgets = {
            'N1': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N2': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N3': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N4': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N5': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N6': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'N7': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer)

        }


class PANSSGeneralForm(forms.ModelForm):
    class Meta:
        model = PANSS
        fields = ('G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16')
        widgets = {
            'G1': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G2': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G3': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G4': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G5': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G6': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G7': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G8': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G9': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G10': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G11': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G12': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G13': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G14': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G15': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),
            'G16': forms.RadioSelect(choices=rating_choices, renderer=HorizontalRadioRenderer),

        }
