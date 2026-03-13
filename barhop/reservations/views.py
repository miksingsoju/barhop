from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Table, Seating, Reservation
<<<<<<< david/reservations
from .forms import SeatingForm
from bars.models import Bar
=======
>>>>>>> main
import json


# TO-DO:
def my_reservations(request):
    if request.method == "GET":
<<<<<<< david/reservations
        reservations = Reservation.objects.filter(hopper=request.user)
        return render(request, "reservations/user-reservations-list.html", {
            'reservations': reservations,
        })

def reservations_list(request, bar_id):
    seatings = Seating.objects.filter(bar__id=bar_id).distinct()
    tables = Table.objects.filter(table_type__in=seatings)
    reservations = Reservation.objects.filter(tables__in=tables).distinct()
    if request.method == "POST":
        status=request.POST.get("rsv_status")
        rsv_id=request.POST.get("rsv_id")
        if rsv_id and status:
            reservation = Reservation.objects.get(id=rsv_id)
            reservation.status = status
            reservation.save()

    return render(request, "reservations/manage-reservations.html", {
        'reservations': reservations,
    })

@login_required
def create_reservation(request, bar_id):
    if request.method == "POST":
        
        date=request.POST.get("rsv_date")
        start_time=request.POST.get("rsv_start_time")
        end_time=request.POST.get("rsv_end_time")

        reservations = Reservation.objects.filter(
            date=date,
            start_time__lt=end_time,
            end_time__gte=start_time,
        )

        r = Reservation.objects.create(
            hopper=request.user,
            guests=request.POST.get("pax"),
            date=request.POST.get("rsv_date"),
            start_time=request.POST.get("rsv_start_time"),
            end_time=request.POST.get("rsv_end_time"),
        )

        selected_seating_ids = request.POST.getlist("selected_tables")
        selected_tables = []
        for id in selected_seating_ids:
            table = Table.objects.filter(table_type_id=id).exclude(reservation__in=reservations).first()
            if table:
                selected_tables.append(table)
        
        print(selected_seating_ids, selected_tables)
        r.tables.add(*selected_tables)

        return redirect('reservations:my-reservations')


def get_avail_tables(request, bar_id):
    avail_tables = Table.objects.filter(table_type__bar__id=bar_id)
    avail_seating = Seating.objects.filter(bar__id=bar_id).distinct()
    if request.method == "POST":
        booking_date = request.POST.get("booking_date")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")

        
        print("date: " + booking_date)
        print("start time: " + start_time)
        print("end time: " + end_time)

        # get all reservations for selected date
        # where time period overlaps selected time
        # note that the tables here cannot be booked
        reservations = Reservation.objects.filter(
            date=booking_date,
            start_time__lt=end_time,
            end_time__gte=start_time,
        )

        # get all tables not under reservation
        # where bar is this bar

        # get all table types of available tables
        reserved_tables = Table.objects.filter(reservation__in=reservations).values_list("id", flat=True)
        avail_tables = Table.objects.filter(table_type__bar__id=bar_id).exclude(id__in=reserved_tables)
        avail_seating = Seating.objects.filter(bar__id=bar_id, table__id__in=avail_tables.values_list("id", flat=True)).distinct()

        print(reservations)
        print(avail_tables)
        print(avail_seating)

        # TO-DO: save form data into session so form doesn't reset on reload
        # request.session['avail_seating'] = list(avail_seating.values_list('pk', flat=True))
        # print(request.session['avail_seating'])

        ctx = {
            "booking_date": booking_date,
            "start_time": start_time,
            "end_time": end_time,
            "bar_id": bar_id,
            "avail_seating": avail_seating,
        }
        return render(request, "reservations/create-booking.html#booking_form_tables", ctx)
    else:
        return {"avail_seating": avail_seating, "avail_tables": avail_tables, }


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
        if (res.status_code >= 400):
            return HttpResponse("error creating table types", status=400)

        seatings = Seating.objects.filter(bar=bar)
        new_tables = [Table(table_type=s) for i, s in enumerate(seatings) for _ in range(int(bar_tables[i]["quantity"]))]
        Table.objects.bulk_create(new_tables)

        print("new_tables", new_tables)
        return HttpResponse("tables created", status=201)
    else:
        return tables

@login_required
def manage_tables(request, bar_id):
    bar = get_object_or_404(Bar, id=bar_id)

    if bar.bar_owner != request.user:
        return redirect('bars:bar-details', pk=bar_id)

    seatings = Seating.objects.filter(bar=bar).prefetch_related('table_set')
    add_form = SeatingForm()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add_seating':
            add_form = SeatingForm(request.POST, request.FILES)
            if add_form.is_valid():
                seating = add_form.save(commit=False)
                seating.bar = bar
                seating.save()
                quantity = add_form.cleaned_data['quantity']
                Table.objects.bulk_create([
                    Table(table_type=seating) for _ in range(quantity)
                ])
                return redirect('reservations:manage-tables', bar_id=bar_id)

        elif action == 'delete_seating':
            seating_id = request.POST.get('seating_id')
            Seating.objects.filter(id=seating_id, bar=bar).delete()
            return redirect('reservations:manage-tables', bar_id=bar_id)

        elif action == 'update_seating':
            seating_id = request.POST.get('seating_id')
            seating = get_object_or_404(Seating, id=seating_id, bar=bar)
            form = SeatingForm(request.POST, request.FILES, instance=seating)
            if form.is_valid():
                form.save()
                new_quantity = form.cleaned_data['quantity']
                current_quantity = seating.table_set.count()
                if new_quantity > current_quantity:
                    Table.objects.bulk_create([
                        Table(table_type=seating) for _ in range(new_quantity - current_quantity)
                    ])
                elif new_quantity < current_quantity:
                    ids_to_delete = list(seating.table_set.values_list('id', flat=True)[:current_quantity - new_quantity])
                    Table.objects.filter(id__in=ids_to_delete).delete()
            return redirect('reservations:manage-tables', bar_id=bar_id)

    seating_forms = [
        (seating, SeatingForm(instance=seating, initial={'quantity': seating.table_set.count()}))
        for seating in seatings
    ]
=======
        Reservation.objects.filter(hopper=request.user)
        return render(request, "reservations/user-reservations-list.html")


@login_required
def create_reservation(request, bar_id):
    if request.method == "POST":
        r = Reservation.objects.create(
            hopper=request.user,
            guests=request.POST.get("pax"),
            date=request.POST.get("rsv_date"),
            start_time=request.POST.get("rsv_start_time"),
            end_time=request.POST.get("rsv_end_time"),
        )

        selected_seating_ids = request.POST.getlist("selected_tables")
        selected_tables = []
        for id in selected_seating_ids:
            selected_tables.append(*Table.objects.filter(table_type__id=id)[:1])
        
        print(selected_seating_ids, selected_tables)
        r.tables.add(*selected_tables)

        return redirect('reservations:my-reservations')


def get_avail_tables(request, bar_id):
    if request.method == "POST":
        booking_date = request.POST.get("booking_date")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")

        # get all reservations for selected date
        # where time period overlaps selected time
        # note that the tables here cannot be booked
        reservations = Reservation.objects.filter(
            date=booking_date,
            start_time__lt=end_time,
            end_time__gte=start_time,
        )

        # get all tables not under reservation
        # where bar is this bar
        avail_tables = Table.objects.exclude(id__in=reservations).filter(table_type__bar__id=bar_id)

        # get all table types of available tables
        avail_seating = Seating.objects.filter(bar__id=bar_id, table__id__in=avail_tables)
        
        print(reservations)
        print(avail_tables)
        print(avail_seating)

        # TO-DO: save form data into session so form doesn't reset on reload
        # request.session['avail_seating'] = list(avail_seating.values_list('pk', flat=True))
        # print(request.session['avail_seating'])

        ctx = {
            "booking_date": booking_date,
            "start_time": start_time,
            "end_time": end_time,
            "bar_id": bar_id,
            "avail_seating": avail_seating,
        }
        return render(request, "reservations/create-booking.html#booking_form_tables", ctx)
    else:
        return {"avail_seating": avail_seating, "avail_tables": avail_tables, }


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
        if (res.status_code >= 400):
            return HttpResponse("error creating table types", status=400)

        seatings = Seating.objects.filter(bar=bar)
        new_tables = [Table(table_type=s) for i, s in enumerate(seatings) for _ in range(int(bar_tables[i]["quantity"]))]
        Table.objects.bulk_create(new_tables)

        print("new_tables", new_tables)
        return HttpResponse("tables created", status=201)
    else:
        return tables
>>>>>>> main

    return render(request, 'reservations/manage-table.html', {
        'bar': bar,
        'seating_forms': seating_forms,
        'add_form': add_form,
    })

# @login_required
def create_seating_form(request):
    return render(request, "reservations/create-bar.html")
