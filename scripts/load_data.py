import csv

from customers.models import Customer


def run():
    fhand = open("tables/customers.csv")
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Customer.objects.all().delete()

    for cnt, row in enumerate(reader, start=1):
        # print(row)
        c = Customer(
            first_name=row[0].strip(),
            last_name=row[1].strip(),
            email=row[2].strip(),
        )
        c.save()
        print(f"'\r' {cnt} Rows processed.", end="")
    print("\n")
