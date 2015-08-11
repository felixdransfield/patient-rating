from django.contrib import admin

# Register your models here.
from panss.models import FullPANSS, PANSS
admin.site.register(PANSS)
admin.site.register(FullPANSS)