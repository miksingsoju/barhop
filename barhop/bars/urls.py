from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.bar_list, name='bar-list'),
    path('create/', views.create_bar, name='create-bar'),
    path('<int:bar_id>/', include([
        path('', views.bar_details, name='bar-details'),
        path('update', views.bar_update, name='bar-update'),
        path('like', views.toggle_like, name='toggle-like'),
        path('reviews/', include('reviews.urls', namespace="reviews")),
        path('reservations/', include('reservations.urls', namespace="reservations")),
        path('events/', include([
            path('create', views.create_event, name='create-event'),
            path('<int:event_id>/update', views.update_event, name='update-event'),
            path('<int:event_id>/delete', views.update_event, name='delete-event'),
        ])),
    ])),
]

app_name = "bars"