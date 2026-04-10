from django.urls import path
from . import views

urlpatterns = [
    # temporary urls
    path('bar/<int:bar_id>/', views.reservations_list, name='bar-tables'),
    path('bar/<int:bar_id>/tables', views.get_avail_tables, name='get-avail-tables'),
    path('bar/<int:bar_id>/create', views.create_reservation, name='create-reservation'),
    path('', views.my_reservations, name='my-reservations'),
    path('bars/<int:bar_id>/tables/manage/', views.manage_tables, name='manage-tables'),
]

app_name = "reservations"