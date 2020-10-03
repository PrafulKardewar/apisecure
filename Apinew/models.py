from django.db import models





class Customer(models.Model):
    name=models.CharField('cust_name',max_length=100)
    age=models.IntegerField('cust_age')
    mob_no=models.IntegerField('cust_mo')
    address=models.CharField('cust_address',max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Bank(models.Model):
    name=models.CharField('bank_name',max_length=100)
    code=models.IntegerField('bank_code')
    acount=models.IntegerField('bank_acc')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Product(models.Model):
    name=models.CharField('prod_name',max_length=100)
    qty=models.IntegerField('prod_qty')
    price=models.FloatField('cust_mo')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)