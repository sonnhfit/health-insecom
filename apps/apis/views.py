from django.shortcuts import render
from rest_framework.views import APIView
from apps.healthapp.models import CustomerParent, ProductCompareHealth
from .serializers import KeySerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
# Create your views here.


class GetAllCustomerParent(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):

        validate = KeySerializer(data=request.data)
        if not validate.is_valid():
            return Response('may gui sai du lieu roi', status=status.HTTP_400_BAD_REQUEST)

        age = validate.data['age']
        id_products = int(validate.data['id_products'])
        prod = ProductCompareHealth.objects.get(id=id_products)
        email = validate.data['email']
        name_user = validate.data['name_user']
        full_name = validate.data['full_name']
        phone = validate.data['phone']
        sex = validate.data['sex']
        city = validate.data['city']
        birth_day = validate.data['birth_day']
        weight = validate.data['weight']
        height = validate.data['height']
        occupation = validate.data['occupation']
        CustomerParent.objects.create(age=age,id_products=prod,email=email,name_user=name_user,
        full_name=full_name,phone=phone,sex=sex,city=city,birth_day=birth_day,
        weight=weight,height=height,occupation=occupation)
        return Response('them thanh cong', status=status.HTTP_200_OK)

