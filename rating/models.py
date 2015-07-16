from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.utils import timezone

# Create your models here.

#Model for Patient Instance
class Patient(models.Model):
    name = models.CharField(max_length=10)
    hospital_id = models.IntegerField(
        # validators=[
        # MaxLengthValidator(10),
        # MinLengthValidator(10)
        #]
    )
    DOB = models.DateField('date of birth', default=timezone.now, blank=True)
    DOA = models.DateField('date of admission', default=timezone.now, blank=True)
    DOD = models.DateField('date of discharge', default=timezone.now, blank=True)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

#Model for PANSS Instance
class PANSS(models.Model):
    rating_date = models.DateField('date of rating', default=timezone.now, blank=True)
    P1 = models.IntegerField('P1 - Delusions', default=0)
    P2 = models.IntegerField('P2 - Conceptual Disorganisation', default=0)
    P3 = models.IntegerField('P3 - Hallucinatory Behaviour', default=0)
    P4 = models.IntegerField('P4 - Excitement', default=0)
    P5 = models.IntegerField('P5 - Grandiosity', default=0)
    P6 = models.IntegerField('P6 - Suspiciousness/Persecution', default=0)
    P7 = models.IntegerField('P7 - Hostility', default=0)
    N1 = models.IntegerField('N1 - Blunted Affect', default=0)
    N2 = models.IntegerField('N2 - Emotional Withdrawal', default=0)
    N3 = models.IntegerField('N3 - Poor Rapport', default=0)
    N4 = models.IntegerField('N4 - Passive/Apathetic Social Withdrawal', default=0)
    N5 = models.IntegerField('N5 - Difficulty in Abstract Thinking', default=0)
    N6 = models.IntegerField('N6 - Lack of Spontaneity', default=0)
    N7 = models.IntegerField('N7 - Stereotyped Thinking', default=0)
    G1 = models.IntegerField('G1 - Somatic Concerns', default=0)
    G2 = models.IntegerField('G2 - Anxiety', default=0)
    G3 = models.IntegerField('G3 - Guilt Feelings', default=0)
    G4 = models.IntegerField('G4 - Tension', default=0)
    G5 = models.IntegerField('G5 - Mannerisms and Posturing', default=0)
    G6 = models.IntegerField('G6 - Depression', default=0)
    G7 = models.IntegerField('G7 - Motor Retardation', default=0)
    G8 = models.IntegerField('G8 - Uncooperativeness', default=0)
    G9 = models.IntegerField('G9 - Unusual Though Content', default=0)
    G10 = models.IntegerField('G10 - Disorientation', default=0)
    G11 = models.IntegerField('G11 - Poor Attention', default=0)
    G12 = models.IntegerField('G12 - Lack of Judgement and Insight', default=0)
    G13 = models.IntegerField('G13 - Disturbance of Volition', default=0)
    G14 = models.IntegerField('G14 - Poor Impulse Control', default=0)
    G15 = models.IntegerField('G15 - Preoccupation', default=0)
    G16 = models.IntegerField('G16 - Active Social Avoidance', default=0)
    S1 = models.IntegerField('S1 - Anger', default=0)
    S2 = models.IntegerField('S2 - Difficulty in Delaying Gratification', default=0)
    S3 = models.IntegerField('S3 - Affective Lability', default=0)
    patient = models.ForeignKey(Patient, related_name='patientname')
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return '%s %s' % (self.patient, self.rating_date)

#Model for HCR20 Instance
class HCR20(models.Model):
    rating_date = models.DateTimeField('date of rating', default=timezone.now, blank=True)
    H1 = models.IntegerField('Previous Violence')
    H2 = models.IntegerField('Young Age at First Violent Incident')
    H3 = models.IntegerField('Relationship Instability')
    H4 = models.IntegerField('Employment Problems')
    H5 = models.IntegerField('Substance Use Problems')
    H6 = models.IntegerField('Major Mental Illness')
    H7 = models.IntegerField('Psychopathy')
    H8 = models.IntegerField('Early Maladjustment')
    H9 = models.IntegerField('Personality Disorder')
    H10 = models.IntegerField('Prior Supervision Failure')
    C1 = models.IntegerField('Lack of Insight')
    C2 = models.IntegerField('Negative Attitudes')
    C3 = models.IntegerField('Active Symptoms of Major Mental Illness')
    C4 = models.IntegerField('Impulsivity')
    C5 = models.IntegerField('Unresponsive to Treatment')
    R1 = models.IntegerField('Plans Lack Feasibility')
    R2 = models.IntegerField('Exposure to Destabilizers')
    R3 = models.IntegerField('Lack of Personal Support')
    R4 = models.IntegerField('Noncompliance with Remediation Attempts')
    R5 = models.IntegerField('Depression')
    patient = models.ForeignKey(Patient)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return '%s %s' % (self.patient, self.rating_date)

#Depreceated
class Update(models.Model):
    rating_1 = models.IntegerField()
    rating_2 = models.IntegerField()
    rating_date = models.DateTimeField('date of rating')
    patient = models.ForeignKey(Patient)

