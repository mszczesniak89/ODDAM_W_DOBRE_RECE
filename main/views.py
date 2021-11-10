from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from .models import Donation, Category, Institution


class HomePage(View):
    def get(self, request):
        stats_bags = Donation.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0
        stats_institutions = Donation.objects.values('institution').distinct().count()
        response = render(request, 'index.html',
                          {
                              'stats_bags': stats_bags,
                              'stats_institutions': stats_institutions,
                          })
        return response


class AddDonation(View):
    def get(self, request):
        response = render(request, 'form.html', )
        return response


