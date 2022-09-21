from re import template
from django.shortcuts import render
from django.views import View
# Create your views here.


class AdminDashboardView(View): 
    template_name = 'la'
    def get (self, request):
        print('Merge')
        print("Database admin dashboard")
        return render(request, 'layouts/base.html')    