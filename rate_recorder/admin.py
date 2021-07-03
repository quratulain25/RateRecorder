from django.contrib import admin

from rate_recorder.models import Rates, Bank

# Register your models here.
admin.site.register(Rates)
admin.site.register(Bank)
