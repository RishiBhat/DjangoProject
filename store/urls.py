#this is the store urls which I have created for now yes welcome 


from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .import views 

urlpatterns = [

    path('',views.index,name="Homepage"),
    path('about/',views.about,name='This is the about page'),
    path('services/',views.services,name="This is the service page"),
    path('contact/',views.contact,name="Call us"),
    path('tracker/',views.tracker,name="Tracke your product"),
    path('checkout/',views.checkout,name="Billing"),
    path('search/',views.search,name='Enter your query'),
    path('productview/',views.productview,name="Products we have"),
]
