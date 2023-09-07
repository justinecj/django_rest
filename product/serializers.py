from rest_framework import serializers
from .models import *

class Productserializer (serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class Customer_preferenceserializer (serializers.ModelSerializer):
    class Meta:
        model = Customer_preference
        fields = '__all__'

class Ordersserializer (serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'