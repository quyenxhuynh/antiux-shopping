from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.start, name='anti-start'),
    path('create/', views.create, name="anti-create"),
    path('time/', views.time, name="anti-time"),
    path('test/', views.test, name="anti-test"),
    
    path('instructions/', views.instructions, name="anti-instructions"),
    path('items/', views.items, name="anti-items"),
    path('shop/', views.store, name="anti-store"),
    path('cart/', views.Cart.as_view(), name="anti-cart"),

    path('empty-cart/', views.empty, name="empty-cart"),
    path('add-to-cart/', views.add, name="add-cart"),

    path('check-cart/', views.check_cart, name='check-cart'),
    path('checkout/', auth_views.LoginView.as_view(template_name='anti_app/checkout.html'), name='checkout')
]
