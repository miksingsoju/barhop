from django.urls import path
from . import views


urlpatterns = [
    path('profile/update/', views.update_profile, name="update_profile"),
    path('accounts/register/', views.register, name='register'),
    path('', views.sign_in, name='sign_in'),
   
]

app_name = "user_management"
