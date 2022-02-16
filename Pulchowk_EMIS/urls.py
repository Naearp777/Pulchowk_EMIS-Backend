"""Pulchowk_EMIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Pulchwok_EMIS"
admin.site.site_title = "Pulchwok_EMIS"
admin.site.index_title = "Welcome to Pulchwok_EMIS"

urlpatterns = [
    path("jet/", include("jet.urls", "jet")),
    path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
    path("admin/", admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("customuser.urls")),
    path("", include("classes.urls")),
    path("", include("department.urls")),
    path("", include("notice.urls")),
    path("", include("batch.urls")),
    path("", include("section.urls")),
    path("", include("miscellaenous.urls")),
    path("", include("student.urls")),
    path("", include("teacher.urls")),
    path("", include("assignments.urls")),
    path("", include("class_materials.urls")),
    path("", include("notification.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
