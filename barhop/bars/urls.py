from django.urls import path
from . import views

urlpatterns = [
    path('', views.bar_list, name='bar-list'),
    path('create/', views.create_bar, name='create-bar'),
    path('<int:bar_id>/', views.bar_details, name='bar-details'),
    path('<int:bar_id>/update', views.bar_update, name='bar-update'),
    path('bar/<int:bar_id>/event/create/', views.create_event, name='create-event'),
    path('event/<int:event_id>/update/', views.update_event, name='update-event'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete-event'),
]

app_name = "bars"