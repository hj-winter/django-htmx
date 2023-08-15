from django.db import models
from django.urls import reverse


class ThemeMain(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class ThemeSub(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    theme_main = models.ForeignKey(ThemeMain, on_delete=models.CASCADE)
    theme_sub = models.ForeignKey(ThemeSub, on_delete=models.CASCADE)
    prod_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"pk": self.pk})
