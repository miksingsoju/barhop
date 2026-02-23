from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Seating, Table


def create_table(request):
    if request.method == 'POST':
        seatings = request.POST.get("seat_types")
        seating_objects = []

        for seat in seatings:
            s = Seating(name=seat["seating_name"], capacity=seat["capacity"])
            seating_objects.append(s)
    
    return HttpResponse(JsonResponse(s), status=302)


# @login_required
def create_seating_form(request):
    return render(request, "reservations/create-bar.html")
