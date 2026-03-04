from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Table
import json


def create_tables(request, bar):
    if request.method == "POST":
        bar_tables = json.loads(request.POST.get("bar_tables", ""))

        if not bar_tables:
            return HttpResponse("no tables to create", status=200)

        for table in bar_tables:
            Table.objects.create(
                bar=bar,
                table_type=table["table_type"],
                qty=int(table["quantity"]),
                capacity=int(table["capacity"]),
            )
        
        return HttpResponse("tables created", status=201)
        


# @login_required
def create_seating_form(request):
    return render(request, "reservations/create-bar.html")
