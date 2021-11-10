from django.shortcuts import render
from django.views import View


class HomePage(View):
    def get(self, request):
        response = render(request, 'index.html', )
        return response

    def post(self, request):
        response = render(request, 'index.html', )
        return response


class AddDonation(View):
    def get(self, request):
        response = render(request, 'form.html', )
        return response

    def post(self, request):
        response = render(request, 'form.html', )
        return response

