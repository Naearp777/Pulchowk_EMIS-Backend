from django.contrib import admin

from assignments.models import Give_Assignments,Submit_Assignments

# Register your models here.

class Give_AssignmentsAdmin(admin.ModelAdmin):
    fieldsets=(
        ('Assignment Info',{'fields':('title','description','teacher_files','due_date')}),
        ('Related Users',{'fields':('classes','teacher')}),
    )
    list_display=('title','description','teacher','classes','due_date','created_at','updated_at')
    list_filter=    ('classes','teacher','due_date','created_at','updated_at')
    search_fields= ('title','description','teacher__name','classes__name','due_date','created_at','updated_at') 
    list_per_page=25

class Submit_AssignmentsAdmin(admin.ModelAdmin):
    fieldsets=(
        ('Submission Info',{'fields':('student','assignment','student_files')}),   
    )
    list_display=('student','assignment',)
    list_filter=    ('student','assignment')
    search_fields= ('student__first_name','assignment__title')
    list_per_page=25

admin.site.register(Give_Assignments,Give_AssignmentsAdmin)
admin.site.register(Submit_Assignments,Submit_AssignmentsAdmin)


