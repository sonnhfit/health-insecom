"""health URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from apps.healthapp import views as health_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('compare-health/', health_views.ComapreHealth.as_view(), name='compare_health_url', ),
    path('comapre-prepayment/', health_views.ComaprePrepayment.as_view()),

    path('', health_views.HealthInsurance.as_view()),
]
