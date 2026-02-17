from django.urls import path
from . import views

urlpatterns = [
    path('', views.bar_list, name='bar-list'),
]

app_name = "bars"