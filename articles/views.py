from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views import generic

from .forms import ArticleForm
from .models import Article, ThemeMain

# class IndexView(generic.ListView):
#     template_name = "articles/index.html"
#     context_object_name = "articles"
#
#     def get_queryset(self) -> QuerySet[Any]:
#         return models.Article.objects.all()

theme_main = []


class DetailView(generic.DetailView):
    context_object_name = "article"
    model = Article
    template_name = "articles/detail.html"


class CreateView(SuccessMessageMixin, generic.CreateView):
    form_class = ArticleForm
    template_name = "articles/edit.html"
    success_message = "You sucessully created a new Article!"


def index(request):
    themes = ThemeMain.objects.all().values_list("name").distinct()
    theme_list = []
    if themes:
        theme_list.extend(theme[0] for theme in themes)
    return render(request, "articles/select.html", {"themes": theme_list})


def themes(request):
    global theme_main
    theme_main = request.GET.get("theme_main")
    theme_list = ["Subkategorie"]
    type_list = ["Produkttyp"]
    sub_themes = (
        Article.objects.select_related("theme_main", "theme_sub")
        .filter(theme_main__name=theme_main)
        .values("theme_main__name", "theme_sub__name")
        .distinct()
    )

    if sub_themes:
        theme_list.extend(item["theme_sub__name"] for item in sub_themes)

    return render(request, "htmx/theme_subs.html",
                  {
                      "themes": theme_list,
                      "types": type_list,
                  }
                  )


def themes_sub(request):
    theme_sub = request.GET.get("theme_sub")
    type_list = []
    prod_types = (
        Article.objects.select_related("theme_main", "theme_sub", "prod_type")
        .filter(theme_main__name=theme_main, theme_sub__name=theme_sub)
        .values("theme_sub__name", "prod_type__name")
        .distinct()
    )

    if prod_types:
        type_list.extend(item["prod_type__name"] for item in prod_types)

    print(prod_types)
    return render(request, "htmx/prod_types.html", {"types": type_list})
