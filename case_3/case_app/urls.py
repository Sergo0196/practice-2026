"""
URL configuration for case_app project.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("my_app.urls")),
]

handler403 = "my_app.views.page_forbidden"
handler404 = "my_app.views.page_not_found"
handler500 = "my_app.views.server_error"
