from django.urls import path
from . import views

urlpatterns = [
    path('', views.bar_list, name='bar-list'),
    path('create/', views.create_bar, name='create-bar'),
    path('user/<slug:username>/', views.bar_list, name='bar-list'),
    path('<int:bar_id>/', views.bar_details, name='bar-details'),
    path('<int:bar_id>/update', views.bar_update, name='bar-update'),
]

app_name = "bars"