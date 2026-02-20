from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Seating, Table


def test():
    print("hello")


# @login_required
def create_seating(request):
    if request.method == 'POST':
        # user_name = request.POST.get("user_name", "")
        pass

    ctx = {
        "stepper": [
            {
                "num": "3",
                "title": "Define Seating",
                "desc": "What types of seating does your bar have?"
            },
            {
                "num": "4",
                "title": "Add Tables",
                "desc": "Setup your bar's reservation system."
            }
        ],
    }

    return render(request, "reservations/create-seating.html", ctx)
