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








#Model for HCR20 Instance
class HCR20(models.Model):
    rating_date = models.DateField('date of rating', default=timezone.now, blank=True)
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

