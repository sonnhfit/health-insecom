from django.shortcuts import render
from django.views import View
# Create your views here.
class indexclass(View):
    def get(seft,request):
         return render(request,"homepage.html")