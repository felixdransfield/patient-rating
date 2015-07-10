from django.contrib import admin

# Register your models here.
from rating.models import Patient, Update, PANSS
admin.site.register(Patient)
admin.site.register(Update)
admin.site.register(PANSS)