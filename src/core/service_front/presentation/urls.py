"""Defines paths to access landing page based resources
"""
from django.urls import path
from service_front.presentation.landing_page import LandingPageView

app_name = 'service_front'

urlpatterns = [
    path('', LandingPageView.as_view(), name='home')
]
