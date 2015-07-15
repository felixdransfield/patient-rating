from django.db import models

# Create your models here.
class Event(models.Model):
    EVENT_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    patient = models.ForeignKey(Patient)
    DOE = models.DateTimeField('Date of Event', default=timezone.now, blank=True)

    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.name