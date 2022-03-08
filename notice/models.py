from django.db import models
from classes.models import classes
from customuser.models import User
from assignments.models import Give_Assignments
from department.models import department

# Create your models here.
class notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    files = models.FileField(upload_to="notice/files/", null=True)
    publish_to = models.ForeignKey(classes, on_delete=models.CASCADE)
    publish_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Notices"
class Assignmentnotice(models.Model):
    assignment=models.ForeignKey(Give_Assignments, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    publish_to = models.ForeignKey(classes, on_delete=models.CASCADE)
    publish_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Notices"


# class global_notice_with_publish_domain(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     files = models.FileField(upload_to="notice/files/", null=True)
#     publish_to = models.ManyToManyField(User)
#     publish_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publish_by")

#     def __str__(self):
#         return f"{self.title}"

#     class Meta:
#         verbose_name_plural = "Global Notices with publish domain"


class Global_Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    files = models.FileField(upload_to="notice/files/", null=True)
    publish_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publish_by")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Global Notices"


class Department_Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    files = models.FileField(upload_to="notice/files/", null=True)
    publish_to = models.ForeignKey(department, on_delete=models.CASCADE)
    publish_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publish_by_dept")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Department Notices"