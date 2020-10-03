from Apinew.views import *








from rest_framework.routers import SimpleRouter

simple_router=SimpleRouter()

simple_router.register('Customer',Custops)
simple_router.register('Bank',Bankops)
simple_router.register('Product',Prodops)



urlpatterns=simple_router.urls


