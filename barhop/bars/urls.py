from django.urls import path
from . import views

urlpatterns = [
    path('', views.bar_list, name='bar-list'),
    path('create/', views.create_bar, name='create-bar'),
    path('<int:bar_id>/', views.bar_details, name='bar-details'),
    path('<int:bar_id>/update', views.bar_update, name='bar-update'),
    path('reviews/<int:review_id>/update/', views.update_review, name='review-update'),
    path('reviews/<int:review_id>/delete/', views.delete_review, name='review-delete'),
]

app_name = "bars"