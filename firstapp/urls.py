from django.urls import path
from firstapp import views


urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact, name='contact'),
    path('services/',views.services, name='services'),
    path('blogs/',views.blogs, name='blogs'),
    path('customers/',views.customers, name='customers')



]