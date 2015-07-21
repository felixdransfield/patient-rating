from django.db import models
from django.contrib.auth.models import User
from rating.models import Patient
from django.utils import timezone


# Create your models here.



class Event(models.Model):
    EVENT_CHOICES = (
        ('1', 'Medication change'),
        ('2', 'Management plan change'),
        ('3', 'Other Stressor')
    )
    event = models.CharField(max_length=1, choices=EVENT_CHOICES)
    patient = models.ForeignKey(Patient)
    DOE = models.DateTimeField('Date of Event', default=timezone.now, blank=True)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.name