"""Defines paths to access landing page based resources
"""
from django.urls import path
from service_front.presentation.landing_page import landing_page

app_name = 'service_front'

urlpatterns = [
    path('', landing_page, name='home')
]
