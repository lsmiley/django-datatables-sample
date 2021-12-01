from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.OrderItemListView.as_view(), name='orderitem'),
    path('new', views.OrderItemCreateView.as_view(), name='new-orderitem'),
    path('orderitem/<pk>/edit', views.OrderItemUpdateView.as_view(), name='edit-orderitem'),
    path('orderitem/<pk>/delete', views.OrderItemDeleteView.as_view(), name='delete-orderitem'),
]
