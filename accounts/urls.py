from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.registerPage, name="register"),
  path('login/', views.loginPage, name="login"),
  path('logout/', views.logoutPage, name="logout"),
  
  path('', views.home, name='home'),
  path('user/', views.userPage, name="user-page"),  
  path('products/', views.products, name='products'),
  path('customer/<str:idKey>/', views.customer, name='customer'),
  
  path('create_order/<str:idKey>/', views.createOrder, name='create_order'),
  path('update_order/<str:orderID>/', views.updateOrder, name='update_order'),
  path('delete_order/<str:orderID>/', views.deleteOrder, name='delete_order'),
]