from django.shortcuts import render
from django.views import View
from .models import ProductCompareHealth
# Create your views here.


class ComapreHealth(View):

    def get(self, request):
        list_ProductCompareHealth = ProductCompareHealth.objects.all()
        context = {"data":list_ProductCompareHealth}
        print(list_ProductCompareHealth)
        return render(request,'compare/compare_health.html',context)
    
    def post(self, request):
        pass


class ComaprePrepayment(View):

    def get(self, request):
        return render(request,'compare/compare_prepayment.html')
    

class HealthInsurance(View):

    def get(self, request):
        return render(request,'health/HealthInsurance.html')

            
class HealthOder(View):

    def get(self, request):
        return render(request,'health-oder/desktop_Religare.html')


class CompanyInsurance(View):

    def get(self, request):
        return render(request,'company.html')


class InfoPayment(View):

    def get(self, request):
        return render(request,'group-mediclaim/info-payment.html')         


class GroupCompany(View):

    def get(self, request):
        return render(request,'group-mediclaim/group-compayny.html')


class GroupQuestionCompany(View):

    def get(self, request):
        return render(request,'group-mediclaim/group-question-company.html')   


class GroupPaymentCompany(View):

    def get(self, request):
        return render(request,'group-mediclaim/group-payment-company.html')  


class SelectCompany(View):

    def get(self, request):
        return render(request,'life-renewal/select-company.html') 


class PayRenewal(View):

    def get(self, request):
        return render(request,'life-renewal/pay-renewal.html')                                
        

class Home(View):

    def get(self, request):
        return render(request,'home_insuarance/home-insuarance.html')


class PreQuote(View):

    def get(self, request):
        return render(request,'home_insuarance/PreQuote.html')

class Quotes(View):

    def get(self, request):
        return render(request,'home_insuarance/Quotes.html')


class Product(View):

    def get(self, request):
        return render(request,'home_insuarance/Product.html')


class Form(View):

    def get(self, request):
        return render(request,'home_insuarance/form.html')


class Renewals(View):

    def get(self, request):
        return render(request,'renewals/renewals.html')


class HealthQuote(View):

    def get(self, request):
        return render(request,'health-quote-compare/health-quote.html')
