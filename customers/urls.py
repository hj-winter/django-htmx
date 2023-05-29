from django.urls import path

from . import views
from .views import AddCustomerView

app_name = "customers"

urlpatterns = [
    path("", views.index, name="index"),
    path("load_data/", views.load_data, name="load-data"),
    path("add_customer/", AddCustomerView.as_view(), name="add_customer"),
]

htmx_urlpatterns = [path("search/", views.search, name="search")]

urlpatterns += htmx_urlpatterns
