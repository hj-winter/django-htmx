from django.urls import path

from . import views

app_name = "customers"

urlpatterns = [
    path("", views.index, name="index"),
    path("load_data/", views.load_data, name="load-data"),
]

htmx_urlpatterns = [path("search/", views.search, name="search")]

urlpatterns += htmx_urlpatterns
