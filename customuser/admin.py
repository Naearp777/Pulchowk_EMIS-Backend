from django.contrib import admin
from .models import User,ExcelFileUpload
# Register your models here.
admin.site.register(User)
admin.site.register(ExcelFileUpload)