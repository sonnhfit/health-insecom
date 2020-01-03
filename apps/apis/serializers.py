from rest_framework import serializers
# from apps.healthapp.models import CustomerParent


# class GetAllCustomerParentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomerParent
#         fields = ('id', 'title',)


class KeySerializer(serializers.Serializer):
    # key_price = serializers.CharField(max_length=50, required=True)
    age = serializers.IntegerField(required=True)
    id_products = serializers.IntegerField()
    email = serializers.CharField(required=True)
    name_user = serializers.CharField(required=True)
    full_name = serializers.CharField(required=True)
    phone = serializers.CharField()
    sex = serializers.BooleanField()
    city = serializers.CharField()
    birth_day = serializers.CharField()
    weight = serializers.IntegerField()
    height = serializers.IntegerField()
    occupation = serializers.CharField()