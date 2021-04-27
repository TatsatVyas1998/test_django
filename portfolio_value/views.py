from django.shortcuts import render , redirect
from portfolio_value.models import portfolio_value
from portfolio_value.form import add_stock
from yahoo_fin import stock_info as si
import yfinance as yf
from django.contrib import messages

# Create your views here.
def in_portfolio(stock_str, shares, equity):
    stock = portfolio_value.objects.all()
    for obj in stock:
        print("this is the input sting", stock_str)
        if( obj.stock == stock_str):
            print("<-----inside------->")
            obj.shares += shares
            obj.your_equity +=float(equity)
            obj.save()
            return True
    return False


def portfolio( request):

    if request.method == "POST":
        #print(request.POST)
        #print('this is what i get for stock price : ' , si.get_live_price('appl'))
        print(type(request.POST['stock']))
        data = yf.download( tickers = request.POST['stock'])#request.POST['stock'])#request.POST['stock'])
        request.POST = request.POST.copy()
        request.POST['shares'] = float(request.POST['your_equity'])/data['Close'][-1]
        request.POST['total_return'] = 0
        if( in_portfolio(request.POST['stock'], request.POST['shares'],  request.POST['your_equity']) == False):
            form = add_stock(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success( request, ("Success!!"))
            return redirect("portfolio")
        else:
            return redirect("portfolio")
    else:
        portfolio_val = portfolio_value.objects.all



        return render(request, 'portfolio.html', {'portfolio_value' : portfolio_val})#{'all_movers': all_movers})


def sell_asst(request, task_id):
    #print(portfolio_value.objects.get(pk=task_id))
    stock = portfolio_value.objects.get(pk=task_id)
    stock.delete()
    return redirect("portfolio")
