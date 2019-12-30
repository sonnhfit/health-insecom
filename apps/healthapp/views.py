from django.shortcuts import render
from django.views import View
# Create your views here.


class ComapreHealth(View):

    def get(self, request):
        return render(request,'compare/compare_health.html')
    
    def post(self, request):
        pass


class ComaprePrepayment(View):

    def get(self, request):
        return render(request,'compare/compare_prepayment.html')
    
    
class HealthInsurance(View):

    def get(self, request):
        return render(request,'health/HealthInsurance.html')
    