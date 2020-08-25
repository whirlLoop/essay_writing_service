"""Contains landing page views
"""
from django.shortcuts import render
from django.views import View
from frontend.forms import CallToActionForm


class LandingPageView(View):
    landingpage_template = 'landing_page/index.html'
    form_class = CallToActionForm

    def get(self, request):
        """Renders the landing pge
        """
        context = {
            'form': self.form_class
        }
        return render(request, self.landingpage_template, context=context)
