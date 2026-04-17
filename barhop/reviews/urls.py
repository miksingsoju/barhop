from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_or_update_review, name='review-create'),
    path('<int:review_id>/update', views.create_or_update_review, name='review-update'),
    path('<int:review_id>/delete', views.delete_review, name='review-delete'),
]

app_name = "reviews"