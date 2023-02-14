from django.contrib import admin

from tasks.models import Machine, Panne, Curative

# Register your models here.

admin.site.register(Machine)
admin.site.register(Panne)
admin.site.register(Curative)
