from django.shortcuts import render, redirect
from django.http import HttpResponse
from bars.models import Bar, Amenity, BarImage 
from .models import Review
from .forms import CreateReviewForm
from user_management.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import PermissionDenied
from django.contrib import messages

# https://stackoverflow.com/questions/62023710/django-how-to-restrict-a-user-to-put-review-only-once

def list_review(request, bar_id):
    bar_object = Bar.objects.get(id=bar_id)
    reviews = Review.objects.filter(bar=bar_object)

        return render(request, 'bars/bar_details.html', {
        'reviews': reviews,
    })
    
def create_review(request, bar_id):
    bar_object = Bar.objects.get(id=bar_id)
    review_form = CreateReviewForm(request.POST or None)
    bar_user = request.user

    if bar_user.user_type != Profile.UserType.BARHOPPER:
        review_form.add_error(None, "Only Bar Hoppers can make reviews")
        messages.error(request, "Only Bar Hoppers can make reviews")

    if request.method == "POST":
        if Review.objects.filter(bar=bar_object, user=bar_user).exists():
            newest_review = Review.objects.filter(bar=bar_object, user=bar_user).latest('review_date_created')
            if timezone.now() - newest_review.review_date_created <= timedelta(days=3):
                review_form.add_error(None, "You cannot make another review within less than 3 days")
                messages.error(request, "Only Bar Hoppers can make reviews")

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.review_user = bar_user
            review.bar = bar_object
            review.save()

    return render(request, 'bars/bar_details.html', {
        'review_form': review_form,
    })