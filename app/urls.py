# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    re_path(r'^transactions/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.TransactionView.as_view(),
            name='transactions'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    path('acctcust/', views.AcctcustListView.as_view(), name='acctcust'),
    path('acctcust/new', views.AcctcustCreateView.as_view(), name='new-acctcust'),
    path('acctcust/<pk>/edit', views.AcctcustUpdateView.as_view(), name='edit-acctcust'),
    path('acctcust/<pk>/delete', views.AcctcustDeleteView.as_view(), name='delete-acctcust'),

]
