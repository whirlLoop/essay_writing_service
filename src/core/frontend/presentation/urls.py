"""Defines paths to access landing page based resources
"""
from django.urls import path
from frontend.presentation.landing_page import LandingPageView

app_name = 'frontend'

urlpatterns = [
    path('', LandingPageView.as_view(), name='home')
]
