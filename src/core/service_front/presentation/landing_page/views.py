"""Contains landing page views
"""
from django.shortcuts import render


def landing_page(request):
    """Renders the landing page
    """
    return render(request, 'landing_page/index.html')
