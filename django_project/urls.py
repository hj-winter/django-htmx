from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("customers/", include("customers.urls")),
    path("articles/", include("articles.urls")),
]
