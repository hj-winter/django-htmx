from django.contrib import admin

from .models import Article, ProductType, ThemeMain, ThemeSub

admin.site.register(Article)
admin.site.register(ThemeMain)
admin.site.register(ThemeSub)
admin.site.register(ProductType)
