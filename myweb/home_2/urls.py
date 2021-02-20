from django.urls import path
from .views import Homepage,Product,Product_data,addtocart,viewcart,getproducts,prodsearch,getallproducts

urlpatterns= [
    path('info',Homepage),
    path('produts/<str:iid>',Product),
    path('prod',Product_data),
    path('atc',addtocart),
    path('vc',viewcart),
    path('gap',getproducts),
    path('ps',prodsearch),
    path('getall/<str:key>',getallproducts)
]