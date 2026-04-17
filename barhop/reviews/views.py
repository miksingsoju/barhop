from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import PermissionDenied
from .forms import ReviewForm
from .models import Review
from bars.models import Bar


def create_or_update_review(request, bar_id=None, review_id=None):
    bar = Bar.objects.get(id=bar_id)

    if request.POST["action"] == "POST":
        review_form = ReviewForm(request.POST or None)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.review_user = request.user
            review.review_bar = bar
            review.review_rating = request.POST.get('rating')
            review.save()
            print(f"review created by {request.user}")
            return redirect('bars:bar-details', bar_id=bar.id)
        else:
            print(review_form.errors)
            return HttpResponse("form not valid", status=404)

    elif request.POST["action"] == "PUT":
        review = Review.objects.get(id=review_id)
        review_form = ReviewForm(request.POST, instance=review)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.review_rating = request.POST.get('rating')
            review.save()
            print(f"review #{review_id} edited by {request.user}")
            return redirect('bars:bar-details', bar_id=bar.id)
        else:
            print(review_form.errors)
            return HttpResponse("form not valid", status=404)
    else:
        return HttpResponse("No get method", status=404)


def delete_review(request, review_id, bar_id=None,):
    review = Review.objects.get(id=review_id)

    if review.review_user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        bar_id = review.review_bar.id
        review.delete()
        return redirect('bars:bar-details', bar_id=bar_id)

    return render(request, 'reviews/delete-review.html', {'review': review})
