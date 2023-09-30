from django.urls import path 
from .  import views 


urlpatterns = [
    path('',views.index,name='index'),
    path('taxrate',views.rate,name="rate"),
    path('<str:number>',views.taxadd,name="taxadd"),


    
]
