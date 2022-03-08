from django.contrib import admin
from .models import Department_Notice, Global_Notice, notice

# Register your models here.
admin.site.register(notice)
# admin.site.register(global_notice_with_publish_domain)
admin.site.register(Global_Notice)
admin.site.register(Department_Notice)
