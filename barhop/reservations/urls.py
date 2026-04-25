from django.urls import include, path
from . import views

urlpatterns = [
    # path('', views.my_reservations, name='my-reservations'),
    path('', views.reservations_list, name='reservations-list'),
    path('create', views.create_reservation, name='create-reservation'),
    path('tables/', include([
        path('', views.get_avail_tables, name='get-avail-tables'),
        path('manage', views.manage_tables, name='manage-tables'),
    ])),
    path('<int:rsv_id>', include([
        path('', views.reservation_details, name='reservation-details'),
        path('cancel', views.cancel_reservation, name='cancel-reservation'),
    ])),

    # temporary urls
    # path('bar/<int:bar_id>/', views.reservations_list, name='bar-tables'),
    # path('bar/<int:bar_id>/tables', views.get_avail_tables, name='get-avail-tables'),
    # path('bar/<int:bar_id>/create', views.create_reservation, name='create-reservation'),
    # path('bars/<int:bar_id>/tables/manage/', views.manage_tables, name='manage-tables'),
]

app_name = "reservations"