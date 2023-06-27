"""assembleurpc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from assembleapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('courier', views.courier, name='courier'),

    path('adminhome', views.adminhome, name='adminhome'),
    path('admincategory', views.admincategory, name='admincategory'),
    path('adminbrand', views.adminbrand, name='adminbrand'),
    path('adminram', views.adminram, name='adminram'),
    path('admindisplay', views.admindisplay, name='admindisplay'),
    path('adminhdd', views.adminhdd, name='adminhdd'),
    path('adminprocessor', views.adminprocessor, name='adminprocessor'),
    path('adminorder', views.adminorder, name='adminorder'),
    path('adminupdateorder', views.adminupdateorder, name='adminupdateorder'),
    path('adminbranddelete', views.adminbranddelete, name='adminbranddelete'),
    path('admincourier', views.admincourier, name='admincourier'),
    path('adminupdateuser', views.adminupdateuser, name='adminupdateuser'),
    path('adminselectcourier', views.adminselectcourier, name='adminselectcourier'),
    path('adminkeyboard', views.adminkeyboard, name='adminkeyboard'),
    path('adminmouse', views.adminmouse, name='adminmouse'),
    path('adminsmps', views.adminsmps, name='adminsmps'),
    path('adminmotherboard', views.adminmotherboard, name='adminmotherboard'),
    path('admincables', views.admincables, name='admincables'),
    path('admincabinet', views.admincabinet, name='admincabinet'),

    path('customerhome', views.customerhome, name='customerhome'),
    path('customerreq', views.customerreq, name='customerreq'),
    path('customerdisplay', views.customerdisplay, name='customerdisplay'),
    path('customerhdd', views.customerhdd, name='customerhdd'),
    path('customerram', views.customerram, name='customerram'),
    path('customerkeyboard', views.customerkeyboard, name='customerkeyboard'),
    path('customermouse', views.customermouse, name='customermouse'),
    path('customersmps', views.customersmps, name='customersmps'),
    path('customermotherboard', views.customermotherboard, name='customermotherboard'),
    path('customercables', views.customercables, name='customercables'),
    path('customercabinet', views.customercabinet, name='customercabinet'),
    path('customerprocessor', views.customerprocessor, name='customerprocessor'),
    path('customerassemble', views.customerassemble, name='customerassemble'),
    path('payment', views.payment, name='payment'),
    path('customerassembleorder', views.customerassembleorder,
         name='customerassembleorder'),
    path('customerslctpro', views.customerslctpro, name='customerslctpro'),
    path('pin', views.pin, name='pin'),
    path('customercart', views.customercart, name='customercart'),


    path('courierhome', views.courierhome, name='courierhome'),
    path('courierorder', views.courierorder, name='courierorder'),
    path('courierupdate', views.courierupdate, name='courierupdate'),
]
