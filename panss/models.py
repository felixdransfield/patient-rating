from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from rating.models import Patient

# Create your models here.
class FullPANSS(models.Model):
    rating_date = models.DateField('date of rating', default=timezone.now, blank=True)
    P1 = models.IntegerField('P1 - Delusions', default=1)
    P2 = models.IntegerField('P2 - Conceptual Disorganisation', default=1)
    P3 = models.IntegerField('P3 - Hallucinatory Behaviour', default=1)
    P4 = models.IntegerField('P4 - Excitement', default=1)
    P5 = models.IntegerField('P5 - Grandiosity', default=1)
    P6 = models.IntegerField('P6 - Suspiciousness/Persecution', default=1)
    P7 = models.IntegerField('P7 - Hostility', default=1)
    N1 = models.IntegerField('N1 - Blunted Affect', default=1)
    N2 = models.IntegerField('N2 - Emotional Withdrawal', default=1)
    N3 = models.IntegerField('N3 - Poor Rapport', default=1)
    N4 = models.IntegerField('N4 - Passive/Apathetic Social Withdrawal', default=1)
    N5 = models.IntegerField('N5 - Difficulty in Abstract Thinking', default=1)
    N6 = models.IntegerField('N6 - Lack of Spontaneity', default=1)
    N7 = models.IntegerField('N7 - Stereotyped Thinking', default=1)
    G1 = models.IntegerField('G1 - Somatic Concerns', default=1)
    G2 = models.IntegerField('G2 - Anxiety', default=1)
    G3 = models.IntegerField('G3 - Guilt Feelings', default=1)
    G4 = models.IntegerField('G4 - Tension', default=1)
    G5 = models.IntegerField('G5 - Mannerisms and Posturing', default=1)
    G6 = models.IntegerField('G6 - Depression', default=1)
    G7 = models.IntegerField('G7 - Motor Retardation', default=1)
    G8 = models.IntegerField('G8 - Uncooperativeness', default=1)
    G9 = models.IntegerField('G9 - Unusual Though Content', default=1)
    G10 = models.IntegerField('G10 - Disorientation', default=1)
    G11 = models.IntegerField('G11 - Poor Attention', default=1)
    G12 = models.IntegerField('G12 - Lack of Judgement and Insight', default=1)
    G13 = models.IntegerField('G13 - Disturbance of Volition', default=1)
    G14 = models.IntegerField('G14 - Poor Impulse Control', default=1)
    G15 = models.IntegerField('G15 - Preoccupation', default=1)
    G16 = models.IntegerField('G16 - Active Social Avoidance', default=1)
    S1 = models.IntegerField('S1 - Anger', default=1)
    S2 = models.IntegerField('S2 - Difficulty in Delaying Gratification', default=1)
    S3 = models.IntegerField('S3 - Affective Lability', default=1)
    patient = models.ForeignKey(Patient)
    created_by = models.ForeignKey(User)
    is_admission = models.BooleanField()
    is_discharge = models.BooleanField()
    is_current = models.BooleanField()



    # returns name of patient and date for admin purposes
    def __unicode__(self):
        return '%s %s' % (self.patient, self.rating_date)


class PANSSFilter(models.Model):
    P1 = models.BooleanField('Delusions')
    P2 = models.BooleanField('Conceptual Disorganisation')
    P3 = models.BooleanField('Hallucinatory Behaviour')
    P4 = models.BooleanField('Excitement')
    P5 = models.BooleanField('Grandiosity')
    P6 = models.BooleanField('Suspiciousness/Persecution')
    P7 = models.BooleanField('Hostility')
    N1 = models.BooleanField('Blunted Affect')
    N2 = models.BooleanField('Emotional Withdrawal')
    N3 = models.BooleanField('Poor Rapport')
    N4 = models.BooleanField('Passive/Apathetic Social Withdrawal')
    N5 = models.BooleanField('Difficulty in Abstract Thinking')
    N6 = models.BooleanField('Lack of Spontaneity')
    N7 = models.BooleanField('Stereotyped Thinking')
    G1 = models.BooleanField('Somatic Concerns')
    G2 = models.BooleanField('Anxiety')
    G3 = models.BooleanField('Guilt Feelings')
    G4 = models.BooleanField('Tension')
    G5 = models.BooleanField('Mannerisms and Posturing')
    G6 = models.BooleanField('Depression')
    G7 = models.BooleanField('Motor Retardation')
    G8 = models.BooleanField('Uncooperativeness')
    G9 = models.BooleanField('Unusual Though Content')
    G10 = models.BooleanField('Disorientation')
    G11 = models.BooleanField('Poor Attention')
    G12 = models.BooleanField('Lack of Judgement and Insight')
    G13 = models.BooleanField('Disturbance of Volition')
    G14 = models.BooleanField('Poor Impulse Control')
    G15 = models.BooleanField('Preoccupation')
    G16 = models.BooleanField('Active Social Avoidance')
    S1 = models.BooleanField('Anger')
    S2 = models.BooleanField('Difficulty in Delaying Gratification')
    S3 = models.BooleanField('Affective Lability')
    patient = models.ForeignKey(Patient)
    is_current = models.BooleanField()




# Model for PANSS Instance
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
    patient = models.ForeignKey(Patient)
    created_by = models.ForeignKey(User)





    #returns name of patient and date for admin purposes
    def __unicode__(self):
        return '%s %s' % (self.patient, self.rating_date)

