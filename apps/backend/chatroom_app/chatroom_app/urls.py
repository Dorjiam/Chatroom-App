from django.contrib import admin
from django.urls import path, include
from Admin.urls import urlpatterns as admin_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path("Admin/", include(admin_urls))
]
