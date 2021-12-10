# -*- encoding: utf-8 -*-


from django.contrib import admin
from django.urls import path, include  # add this

from django.conf.urls.static import static
from django.conf import settings

from django.views.generic.base import TemplateView

from order.views import ( ajax_add_product, ajax_modify_order_item, ajax_search_products, ajax_calculate_results_view,
                         ajax_calculate_category_view, ajax_get_products )

urlpatterns = [
    # path('admin/', admin.site.urls),          # Django admin route
    path('admin', admin.site.urls),          # Django admin route
    # path('ajax/', include('post.urls')),
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

    #  ajax_calls
    path('ajax/search-products/<int:pk>/', ajax_search_products, name='ajax-search'),
    path('ajax/add-product/<int:pk>/<int:dk>/', ajax_add_product, name='ajax_add'),
    path('ajax/modify-product/<int:pk>/<slug:action>', ajax_modify_order_item, name='ajax_modify'),
    path('ajax/calculate-results/', ajax_calculate_results_view, name='ajax_calculate_result'),
    path('ajax/calculate-category-results/', ajax_calculate_category_view, name='ajax_category_result'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)