from django.shortcuts import render
from Apinew.serialization import *



from rest_framework.viewsets import ModelViewSet
# Create your views here.

class Custops(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSer

class Bankops(ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSer

class Prodops(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSer