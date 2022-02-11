from django.contrib import admin

from assignments.models import Give_Assignments,Submit_Assignments

# Register your models here.
admin.site.register(Give_Assignments)
admin.site.register(Submit_Assignments)
