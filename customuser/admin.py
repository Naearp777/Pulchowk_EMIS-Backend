from django.contrib import admin
from .models import User,ExcelFileUpload
# Register your models here.

admin.site.register(ExcelFileUpload)


class CustomUserAdmin(admin.ModelAdmin):
    fieldsets=(
        ('Login',{'fields':('email','password')}),
        ('Personal Info',{'fields':('first_name','middle_name','last_name','address')}),
        ('Contact Info',{'fields':('phone','dob')}),
        ('Profile Image',{'fields':('images',)}),
        ('Permissions',{'fields':('admin','staff','student')}),
        ('Other Info',{'fields':('password_changed','last_login')}),
    )

admin.site.register(User,CustomUserAdmin)