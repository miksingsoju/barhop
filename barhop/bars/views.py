from django.shortcuts import render, redirect
from .forms import CreateBarForm
from .models import Bar, Amenity #, Address
from user_management.models import Profile
from django.db.models import Case, When, Value, IntegerField
from django.contrib.auth.decorators import login_required



def bar_list(request, username=None):
    user_profile = request.user if request.user.is_authenticated else None
    custom_order = Case(
        When(bar_status='FIRE', then=Value(0)),
        When(bar_status='LUKEWARM', then=Value(1)),
        When(bar_status='COLD', then=Value(2)),
        output_field=IntegerField()
    )
    if username:
        bars = Bar.objects.filter(bar_owner=request.user).annotate(
        status_order=custom_order).order_by('status_order')
    
    if user_profile != None and username == None:
            bars = Bar.objects.exclude(bar_owner=request.user).annotate(
                status_order=custom_order).order_by('status_order')

    if user_profile == None:
         bars = Bar.objects.all().annotate(
            status_order=custom_order).order_by('status_order')

   
    return render(request, 'bars/bar-list.html', {
        'bars': bars,
    })

# @login_required
def create_bar(request):
    bar_form = CreateBarForm(request.POST or None)
    if request.method == "POST":
        if bar_form.is_valid():
            bar = bar_form.save(commit=False)
            bar.bar_owner = request.user
            bar.bar_draft = False
            bar.save()
            return redirect('bars:bar-details', bar_id=bar.id)
    
    bar_form = CreateBarForm()

    ctx = {
        "stepper": [
            {
                "num": "1",
                "title": "Bar Details",
                "desc": "Set up your bar's details.",
                "current": "current",
            },
            {
                "num": "2",
                "title": "Add Events",
                "desc": "What's happening at your bar? Let people know!",
                "current": "",
            },
            {
                "num": "3",
                "title": "Add Tables",
                "desc": "Set up your bar's reservation system.",
                "current": "",
            },
            {
                "num": "4",
                "title": "Publish Your Bar",
                "desc": "Share your bar with the world!",
                "current": "",
            }
        ],
        'bar_form': bar_form,
    }
    return render(request, 'bars/create-bar.html', ctx)
    
def bar_details(request, bar_id):
    bar_object = Bar.objects.get(id=bar_id)
    bar_owner = bar_object.bar_owner == request.user if request.user.is_authenticated else False

    return render(request, 'bars/bar-details.html', {
        'bar': bar_object,
    })

def bar_update(request, bar_id):
    bar_object = Bar.objects.get(id=bar_id)
    if bar_object.bar_owner != request.user:
        return redirect('bars:bar-details', bar_id=bar_id)
    if request.method == 'POST':
        bar_form = CreateBarForm(request.POST, instance=bar_object)
        if bar_form.is_valid():
            bar_form.save()
            return redirect('bars:bar-details', bar_id=bar_id)
    else:
        bar_form = CreateBarForm(instance=bar_object)

    return render(request, 'bars/update-bar.html', {
        'bar_form': bar_form,
    })

