"""Contains landing page views
"""
from django.shortcuts import render
from django.views import View


class LandingPageView(View):
    landingpage_template = 'landing_page/index.html'

    def get(self, request):
        """Renders the landing pge
        """
        return render(request, self.landingpage_template)
