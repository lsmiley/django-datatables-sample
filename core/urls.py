# -*- encoding: utf-8 -*-


from django.contrib import admin
from django.urls import path, include  # add this

from django.conf.urls.static import static
from django.conf import settings

from django.views.generic.base import TemplateView

from order.views import ( ajax_add_product, ajax_modify_order_item, ajax_search_products, ajax_calculate_results_view,
                         ajax_calculate_category_view )

urlpatterns = [
    # path('admin/', admin.site.urls),          # Django admin route
    path('admin', admin.site.urls),          # Django admin route
    # Apps
    path('acctcust', include('acctcust.urls')),
    path('labordeliverytype', include('labordeliverytype.urls')),
    path('labordelivery', include('labordelivery.urls')),
    path('prodvendor', include('prodvendor.urls')),
    path('orderitem', include('orderitem.urls')),
    path('product', include('product.urls')),
    path('order', include('order.urls')),
    path('category', include('category.urls')),

    path('ckeditor', include('ckeditor_uploader.urls')),
    path("", include("authentication.urls")),  # Auth routes - login / register
    path("", include("app.urls")),             # UI Kits Html files

    #   Sizing_calls
    # path('order/order-list/', OrderListView.as_view(), name='order_list'),
    # path('create/', CreateOrderView.as_view(), name='create-order'),
    # path('create-auto/', auto_create_order_view, name='create_auto'),
    # path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='update_order'),
    # path('done/<int:pk>/', done_order_view, name='done_order'),
    # path('delete/<int:pk>/', delete_order, name='delete_order'),
    # path('action/<int:pk>/<slug:action>/', order_action_view, name='order_action'),

    #  ajax_calls
    path('order/ajax/search-products/<int:pk>/', ajax_search_products, name='ajax-search'),
    path('order/ajax/add-product/<int:pk>/<int:dk>/', ajax_add_product, name='ajax_add'),
    path('order/ajax/modify-product/<int:pk>/<slug:action>', ajax_modify_order_item, name='ajax_modify'),
    path('order/ajax/calculate-results/', ajax_calculate_results_view, name='ajax_calculate_result'),
    path('order/ajax/calculate-category-results/', ajax_calculate_category_view, name='ajax_category_result'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)