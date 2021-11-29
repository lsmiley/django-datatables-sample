
from django.urls import path
from acctcust import views


urlpatterns = [


    path('', views.AcctcustListView.as_view(), name='acctcust'),
    path('new', views.AcctcustCreateView.as_view(), name='new-acctcust'),
    path('acctcust/<pk>/edit', views.AcctcustUpdateView.as_view(), name='edit-acctcust'),
    path('acctcust/<pk>/delete', views.AcctcustDeleteView.as_view(), name='delete-acctcust'),

    # # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
