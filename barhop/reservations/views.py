from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Table, Seating
import json


def get_or_create_seatings(request, bar):
    seatings = Seating.objects.filter(bar=bar)

    if request.method == "GET":
        return JsonResponse(seatings, safe=False)
    elif request.method == "POST":
        bar_tables = json.loads(request.POST.get("bar_tables", ""))

        new_seatings = [
            Seating(
                bar=bar,
                seating=table["table_type"],
                capacity=int(table["capacity"])
            ) for table in bar_tables
        ]

        Seating.objects.bulk_create(new_seatings)
        return HttpResponse("seatings created", status=201)
    else:
        return seatings


def get_or_create_tables(request, bar):
    tables = Table.objects.filter(table_type__bar=bar)

    if request.method == "GET":
        return JsonResponse(tables, safe=False)
    if request.method == "POST":
        if not request.POST.get("bar_tables", ""):
            msg = "no tables to create"
            print(msg)
            return HttpResponse(msg, status=204)
        
        bar_tables = json.loads(request.POST.get("bar_tables", ""))

        res = get_or_create_seatings(request, bar)
        if (res >= 400):
            return HttpResponse("error creating table types", status=400)

        seatings = Seating.objects.filter(bar=bar)

        new_tables = [Table(table_type=s) for i, s in enumerate(seatings) for _ in range(int(bar_tables[i]["quantity"]))]
        Table.objects.bulk_create(new_tables)

        print("new_tables", new_tables)
        return HttpResponse("tables created", status=201)
    else:
        return tables


# @login_required
def create_seating_form(request):
    return render(request, "reservations/create-bar.html")
