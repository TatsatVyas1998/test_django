from portfolio_value.models import portfolio_value
import yfinance as yf


def update_portfolio():
    stock = portfolio_value.objects.all()
    for obj in stock:
        data = yf.download( tickers = obj.stock, period = '1d', interval = '2m')
        cur_price = data['Close'][-1]
        cur_val = obj.shares * cur_price
        diff = cur_val-obj.your_equity
        obj.total_return += diff
        obj.your_equity = cur_val
        obj.save()
