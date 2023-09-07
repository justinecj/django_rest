from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.renderers import TemplateHTMLRenderer



# using class
class ArticleAPIView(APIView):
    

    def get(self, request):

        products = Products.objects.all()
        serializer = Productserializer(products, many=True)

        customer_preference = Customer_preference.objects.all()
        serializer1 = Customer_preferenceserializer(customer_preference, many=True)

        orders = Orders.objects.all()
        serializer2 = Ordersserializer(orders, many=True)

        # popular_product =Orders.objects.raw("SELECT * FROM Products WHERE (SELECT COUNT(product_id) FROM Customer_preference); ")
        # print("******")
        # print(popular_product)
        # print("******")

        return Response(serializer.data + serializer1.data + serializer2.data)





