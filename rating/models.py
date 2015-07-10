from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.utils import timezone

# Create your models here.

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


class PANSS(models.Model):
    rating_date = models.DateTimeField('date of rating', default=timezone.now, blank=True)
    P1 = models.IntegerField('Delusions')
    P2 = models.IntegerField()
    P3 = models.IntegerField()
    P4 = models.IntegerField()
    P5 = models.IntegerField()
    P6 = models.IntegerField()
    P7 = models.IntegerField()
    N1 = models.IntegerField()
    N2 = models.IntegerField()
    N3 = models.IntegerField()
    N4 = models.IntegerField()
    N5 = models.IntegerField()
    N6 = models.IntegerField()
    N7 = models.IntegerField()
    G1 = models.IntegerField()
    G2 = models.IntegerField()
    G3 = models.IntegerField()
    G4 = models.IntegerField()
    G5 = models.IntegerField()
    G6 = models.IntegerField()
    G7 = models.IntegerField()
    G8 = models.IntegerField()
    G9 = models.IntegerField()
    G10 = models.IntegerField()
    G11 = models.IntegerField()
    G12 = models.IntegerField()
    G13 = models.IntegerField()
    G14 = models.IntegerField()
    G15 = models.IntegerField()
    G16 = models.IntegerField()
    S1 = models.IntegerField()
    S2 = models.IntegerField()
    S3 = models.IntegerField()
    patient = models.ForeignKey(Patient)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return '%s %s' % (self.patient, self.rating_date)


class Update(models.Model):
    rating_1 = models.IntegerField()
    rating_2 = models.IntegerField()
    rating_date = models.DateTimeField('date of rating')
    patient = models.ForeignKey(Patient)

