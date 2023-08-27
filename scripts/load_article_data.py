import csv

from articles.models import Article, ProductType, ThemeMain, ThemeSub


def run():
    fhand = open("tables/Artikel-Daten-Import.csv")
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    ThemeMain.objects.all().delete()
    ThemeSub.objects.all().delete()
    ProductType.objects.all().delete()
    Article.objects.all().delete()

    cnt = 0
    for cnt, row in enumerate(reader, start=1):
        typ, created = ProductType.objects.get_or_create(name=row[7].strip())
        t_s, created = ThemeSub.objects.get_or_create(name=row[6].strip())
        t_m, created = ThemeMain.objects.get_or_create(name=row[5].strip())

        a = Article(
            name=row[2].strip(),
            number=row[0].strip(),
            description=row[3].strip(),
            theme_main=t_m,
            theme_sub=t_s,
            prod_type=typ,
        )
        a.save()
    print(f"{cnt} Artikel-Daten-Import.csv geladen.")
