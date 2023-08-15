from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("", views.index, name="index"),
    path("<int:pk>", views.DetailView.as_view(), name="detail"),
    path("submit", views.CreateView.as_view(), name="submit"),
]

htmx_views = [
    path("themes/", views.themes, name="themes"),
    path("themes_sub/", views.themes_sub, name="themes_sub"),
]

urlpatterns += htmx_views
