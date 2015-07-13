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
    DOB = models.DateTimeField('date of birth', default=timezone.now, blank=True)
    DOA = models.DateTimeField('date of admission', default=timezone.now, blank=True)
    DOD = models.DateTimeField('date of discharge', default=timezone.now, blank=True)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

#Model for PANSS Instance
class PANSS(models.Model):
    rating_date = models.DateTimeField('date of rating', default=timezone.now, blank=True)
    P1 = models.IntegerField(verbose_name='Delusions')
    P2 = models.IntegerField('Conceptual Disorganisation')
    P3 = models.IntegerField('Hallucinatory Behaviour')
    P4 = models.IntegerField('Excitement')
    P5 = models.IntegerField('Grandiosity')
    P6 = models.IntegerField('Suspiciousness/Persecution')
    P7 = models.IntegerField('Hostility')
    N1 = models.IntegerField('Blunted Affect')
    N2 = models.IntegerField('Emotional Withdrawal')
    N3 = models.IntegerField('Poor Rapport')
    N4 = models.IntegerField('Passive/Apathetic Social Withdrawal')
    N5 = models.IntegerField('Difficulty in Abstract Thinking')
    N6 = models.IntegerField('Lack of Spontaneity')
    N7 = models.IntegerField('Stereotyped Thinking')
    G1 = models.IntegerField('Somatic Concerns')
    G2 = models.IntegerField('Anxiety')
    G3 = models.IntegerField('Guilt Feelings')
    G4 = models.IntegerField('Tension')
    G5 = models.IntegerField('Mannerisms and Posturing')
    G6 = models.IntegerField('Depression')
    G7 = models.IntegerField('Motor Retardation')
    G8 = models.IntegerField('Uncooperativeness')
    G9 = models.IntegerField('Unusual Though Content')
    G10 = models.IntegerField('Disorientation')
    G11 = models.IntegerField('Poor Attention')
    G12 = models.IntegerField('Lack of Judgement and Insight')
    G13 = models.IntegerField('Disturbance of Volition')
    G14 = models.IntegerField('Poor Impulse Control')
    G15 = models.IntegerField('Preoccupation')
    G16 = models.IntegerField('Active Social Avoidance')
    S1 = models.IntegerField('Anger')
    S2 = models.IntegerField('Difficulty in Delaying Gratification')
    S3 = models.IntegerField('Affective Lability')
    patient = models.ForeignKey(Patient)
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

