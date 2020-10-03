from Apinew.models import *
from rest_framework.serializers import ModelSerializer




class CustomerSer(ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"

class BankSer(ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"

class ProductSer(ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
