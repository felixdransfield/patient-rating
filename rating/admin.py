from django.contrib import admin

# Register your models here.
from rating.models import Patient, HCR20, PANSS
admin.site.register(Patient)
admin.site.register(HCR20)
admin.site.register(PANSS)