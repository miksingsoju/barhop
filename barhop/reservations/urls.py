from django.urls import path
from . import views

urlpatterns = [
    # temporary url
    path('seating/create', views.create_seating, name='create-seating'),
]

app_name = "reservations"