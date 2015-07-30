from django.db import models
from django.contrib.auth.models import User
from rating.models import Patient
from django.utils import timezone


# Create your models here.



class Event(models.Model):
    event_type = models.CharField(max_length=1)
    event_description = models.CharField(max_length=200)
    patient = models.ForeignKey(Patient)
    DOE = models.DateField('Date of Event', default=timezone.now, blank=True)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.name