from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from django.views.generic import ListView
# Create your views here.
import pandas as pd
import numpy as np
from predictive_models.models import load_stocks , selected_stocks , created_portfolio
import json
from predictive_models.form import add_stock
from predictive_models.markowitz_portfolio_opt import get_opt_portfolio
import ast

def predictive_models_veiw( request):
    print("<-------this is load stocks return---->",load_stocks.objects.count())
    form = add_stock()
    #print(json.dumps(list(load_stocks.objects.values())))
    if request.method == "POST":
        searched = request.POST['searched']
        queryset = load_stocks.objects.filter(stock_name__icontains=searched)
        symbol = queryset[0].stock_symbol
        #mylist += [x.stock_symbol for x in queryset]
        obj = selected_stocks.objects.create(stock_name = searched , stock_symbol = symbol)
        obj.save()
        print("<---------got the post-------->" , symbol)
    if(load_stocks.objects.count() ==0):
        df = pd.read_csv("/home/tatsat/django_test/test_django/predictive_models/docs/stock_list.csv")
        for i, row in df.iterrows():
            obj = load_stocks.objects.create(stock_name = row['Name'] , stock_symbol= row['Symbol'] )
            obj.save()
    print("<------redicrecting-------->")
    selected_stocks_val = selected_stocks.objects.all
    return render(request, './predictive_models/load_stocks_list.html', {'selected_stocks': selected_stocks_val})


def portfolio_testing(request):

    created_portfolio_val = created_portfolio.objects.all
    return render(request, './predictive_models/portfolio_testing.html', {'created_portfolio' : created_portfolio_val})


class stock_view(ListView):
    model = load_stocks

    #template_name = 'predictive_models.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["qs_json"]= json.dumps(list(load_stocks.objects.values()))
        return context



def autosuggest(request):
    print(request.GET)
    query_original = request.GET.get('term')
    queryset = load_stocks.objects.filter(stock_name__icontains=query_original)
    mylist = []
    mylist += [x.stock_name for x in queryset]
    return JsonResponse(mylist , safe = False)

def create_portfolio(request):
    all_selected = selected_stocks.objects.all()
    markovitz_lst = []
    for obj in all_selected:

        markovitz_lst.append(obj.stock_symbol)
    opt_w = get_opt_portfolio(markovitz_lst)
    print("<------This is the final list------->" , markovitz_lst)
    obj = created_portfolio.objects.create()
    obj.add_symbol(markovitz_lst)
    obj.add_opt_weights(list(opt_w))
    obj.save()
    selected_stocks.objects.all().delete()
    return redirect("predictive_models")

def included_stocks(request, task_id):
    stock = created_portfolio.objects.get(pk=task_id)
    print("<---this is the stock---->" , ast.literal_eval(stock.stock_symbol))
    #return redirect("portfolio_testing")

    return render(request, './predictive_models/included_stocks.html', {'included_stocks': ast.literal_eval(stock.stock_symbol)})
class portfolio_weights_help:
    """docstring for ."""
    def __init__(self, stock , weight):
        self.stock = stock
        self.weights=weight


def portfolio_weights(request, task_id):
    stock = created_portfolio.objects.get(pk=task_id)
    print("<---this is the stock---->" , ast.literal_eval(stock.stock_symbol))
    #return redirect("portfolio_testing")
    obj_lst = []
    stock_list = ast.literal_eval(stock.stock_symbol)
    weight_list = ast.literal_eval(stock.port_weight_opt)
    for i in range(0, len(weight_list)) :
        #tmp = portfolio_weights_help
        #tmp.stock = stock_list[i]
        #tmp.weights = float(weight_list[i]) *100
        obj_lst.append( portfolio_weights_help(stock_list[i] , float(weight_list[i]) *100))

    return render(request, './predictive_models/portfolio_weights.html', {'included_stocks': obj_lst})



def invest(request):
    return redirect("portfolio_testing")

"""
def add_stock(request):
    print("<---------got the post-------->")
    print(request.method)
    return render(request,"./predictive_models/load_stocks_list.html" , {})
"""
