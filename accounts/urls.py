from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('register/', views.registerPage, name="register"),
  path('login/', views.loginPage, name="login"),
  path('logout/', views.logoutPage, name="logout"),
  
  path('', views.home, name='home'),
  path('user/', views.userPage, name="user-page"),
  path('account/', views.accountSettings, name="account"),  
  path('products/', views.products, name='products'),
  path('customer/<str:idKey>/', views.customer, name='customer'),
  
  path('create_order/<str:idKey>/', views.createOrder, name='create_order'),
  path('update_order/<str:orderID>/', views.updateOrder, name='update_order'),
  path('delete_order/<str:orderID>/', views.deleteOrder, name='delete_order'),
  
  path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset-password'),
  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password-reset-done'),
  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),
]