from django.db.models import Q
from django.shortcuts import render

from .models import Customer


def index(request):
    # customers = Customer.objects.all()[:20]
    # context = {"customers": customers}
    return render(request, "customers/index.html")


def load_data(request):
    customers = Customer.objects.all()
    context = {"customers": customers}
    return render(request, "customers/data_list.html", context)


def search(request):
    search_item = request.POST.get("query")
    context = {}
    if search_item:
        results = Customer.objects.filter(
            Q(first_name__icontains=search_item)
            | Q(last_name__icontains=search_item)
            | Q(email__icontains=search_item)
        )
        context = {"results": results}
    return render(request, "customers/search_results.html", context)
