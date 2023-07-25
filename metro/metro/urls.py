"""metro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from metroapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),

    path('login',views.login),
    path('loginCus',views.loginCus),
    path('waterBook',views.waterBook),
    path('metroBook',views.metroBook),

    path('register',views.register),
    path('adminaddflights',views.adminaddflights),
    path('adminhome',views.adminhome),
    path('adminHom',views.adminHom),
    path('addService',views.addService),
    path('addStation',views.addStation),
    path('feedBus',views.feedBus),
    path('addWStation',views.addWStation),
    path('schedulesMetro',views.schedulesMetro),

    path('adminpayment',views.adminpayment),
    path('adminvbooking',views.adminvbooking),
 
    path('upayment',views.upayment),
    path('userpay',views.userpay),
    path('feederPay',views.feederPay),
    path('poolPay',views.poolPay),
    path('cabPay',views.cabPay),
    path('cabBook',views.cabBook),
    path('schedule',views.schedule),
    path('userwpay',views.userwpay),
    path('adminbooking',views.adminbooking),
    path('bookFood',views.bookFood),
    path('adminfood',views.adminfood),
    path('ubooking',views.userbooking),
    path('userhome',views.userhome),
  
    path('userbooking',views.userbooking),
    path('uservflights',views.uservflights),
    path('userpayment',views.userpayment),
    path('bill',views.bill),
    path('billw',views.billw),
    path('chart',views.chart),

]
