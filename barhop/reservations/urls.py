from django.urls import path
from . import views

urlpatterns = [
    # temporary urls
    # path('bar/<int:bar_id>', views.bar_reservations_list, name='bar-tables'),
    path('bar/<int:bar_id>/tables', views.get_avail_tables, name='get-avail-tables'),
    path('bar/<int:bar_id>/create', views.create_reservation, name='create-reservation'),
    path('', views.my_reservations, name='my-reservations'),
]

app_name = "reservations"