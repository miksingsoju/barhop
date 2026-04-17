from django.urls import include, path
from . import views
from reviews import views as rv

urlpatterns = [
    path('', views.bar_list, name='bar-list'),
    path('create/', views.create_bar, name='create-bar'),
    path('<int:bar_id>/', views.bar_details, name='bar-details'),
    path('<int:bar_id>/update', views.bar_update, name='bar-update'),
    path('<int:bar_id>/reviews/', include('reviews.urls', namespace="reviews")),
]

app_name = "bars"