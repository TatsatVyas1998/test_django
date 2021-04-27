from django.shortcuts import render
from django.http import HttpResponse
from portfolio_value.models import portfolio_value


def home_page( request):
    return render(request, 'home_page.html', {})

def get_stock_data( request , *args , **kwargs ):

    portfolio_val = portfolio_value.objects.all
    return JsonResponse()
