"""
URL configuration for barhop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('__reload__/', include('django_browser_reload.urls')),
    path('', RedirectView.as_view(url='/bars/', permanent=False)),
    path('', include('django.contrib.auth.urls')),
    path('user/', include('user_management.urls', namespace="auth")),
    path('admin/', admin.site.urls),
    path('bars/', include('bars.urls', namespace="bars")),
    path('reservations/', include('reservations.urls', namespace="reservations")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
