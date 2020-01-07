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
from apps.apis import views as apis_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comapre-prepayment/', health_views.ComaprePrepayment.as_view(),name='comapre_prepayment_url'),
    path('health-insurance/', health_views.HealthInsurance.as_view()),
    path('compare-health/', health_views.ComapreHealth.as_view(), name='compare_health_url'),
    path('health-oder/', health_views.HealthOder.as_view(), name='health-oder_url'),
    path('', health_views.HealthInsurance.as_view()),
    path('health-add/', apis_views.GetAllCustomerParent.as_view()),
    path('group-company/', health_views.GroupCompany.as_view(), name='group-company_url'),
    path('group-question-company/', health_views.GroupQuestionCompany.as_view(), name='group-question-company_url'),
    path('group-payment-company/', health_views.GroupPaymentCompany.as_view(), name='group-payment-company_url'),
    path('info-payment/', health_views.InfoPayment.as_view(), name='info-payment_url'),
    path('company/', health_views.CompanyInsurance.as_view(), name='company_url'),
    path('select-company/', health_views.SelectCompany.as_view(), name='select-company_url'),
    path('pay-renewal/', health_views.PayRenewal.as_view(), name='pay-renewal_url')
    
]
