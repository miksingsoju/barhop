from django.urls import path
from . import views


urlpatterns = [
    path('', views.update_profile, name="update_profile"),
    path('register/', views.register, name='register'),

]

app_name = "user_management"
