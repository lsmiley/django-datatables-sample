# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

from order.views import HomepageView, OrderListView, CreateOrderView, auto_create_order_view, OrderItemUpdateView, OrderUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path('admin', admin.site.urls),          # Django admin route
    # Apps
    path('acctcust', include('acctcust.urls')),
    path('labordeliverytype/', include('labordeliverytype.urls')),
    path('labordelivery/', include('labordelivery.urls')),
    path('prodvendor/', include('prodvendor.urls')),
    path('orderitem/', include('orderitem.urls')),
    path('product/', include('product.urls')),
    path('category/', include('category.urls')),
    path('', HomepageView.as_view(), name='homepage'),
    path('order-list/', OrderListView.as_view(), name='order_list'),
    path('create/', CreateOrderView.as_view(), name='create-order'),
    path('create-auto/', auto_create_order_view, name='create_auto'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update_order'),
    path('updateitem/<int:pk>/', OrderItemUpdateView.as_view(), name='update_orderitem'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),             # UI Kits Html files



]
