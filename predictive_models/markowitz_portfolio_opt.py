import yfinance as yf
import pandas.util.testing as tm
import pandas as pd
import datetime
import numpy as np
from scipy.optimize import minimize
"""
stocks= ['MSFT','AAPL', 'GOOG', 'GOOGL' , 'FB' , 'NVDA' , 'INTC'  ]

df = pd.DataFrame()
for stock in stocks:
    data = yf.Ticker(stock)
    prices = data.history(period= '1d' , start = '2010-1-1' , end= '2020-1-25')
    if( df.empty):
        df = prices['Close'].to_frame()
    else:
        df = pd.concat([df['Close'],prices['Close']], axis = 1)

#print(df)
rt = np.log(df/df.shift(1))
print(rt.head())
rt = rt.iloc[1:]
#print(df.head())
n_port = 1000
exp_r = np.zeros(n_port)
exp_vol = np.zeros(n_port)
sharp = np.zeros(n_port)

w_t = np.zeros((n_port,len(stocks)))
for k in range(n_port):
    w = np.array(np.random.random(len(stocks)))
    w =w / np.sum(w)
    w_t[k,:] = w
    exp_r[k]=np.sum(rt.mean()*w)
    exp_vol[k]= np.sqrt(np.dot(w.T, np.dot( rt.cov() , w)))
    sharp[k]= exp_r[k]/exp_vol[k]

"""

#print(exp_r)

def sum_one(w):
    return np.sum(w)-1
def get_opt_portfolio(stocks):


    df = pd.DataFrame()
    for stock in stocks:
        data = yf.Ticker(stock)
        prices = data.history(period= '1d' , start = '2010-1-1' , end= '2020-1-25')
        if( df.empty):
            df = prices['Close'].to_frame()
        else:
            df = pd.concat([df['Close'],prices['Close']], axis = 1)

    #print(df)
    rt = np.log(df/df.shift(1))
    print(rt.head())
    rt = rt.iloc[1:]
    #print(df.head())
    n_port = 1000
    exp_r = np.zeros(n_port)
    exp_vol = np.zeros(n_port)
    sharp = np.zeros(n_port)
    def minusSR(w):
        w = np.array(w)
        sr = np.sum(rt.mean()*w)/ np.sqrt(np.dot(w.T, np.dot( rt.cov() , w)))
        return -1*sr
    w_0 = list(np.random.rand(len(stocks)))
    B = []
    for i in range(len(stocks)):
        B.append((0,1))
    B = tuple(B)
    cnt = ({'type':'eq', 'fun': sum_one})
    w = minimize( minusSR    , w_0, method = 'SLSQP' , bounds = B , constraints = cnt)
    return(w.x)

#print(w.x)

"""
rt_arr = np.linspace(0,1, 50)
volatility_opt = []

def min_vol(w):
    w = np.array(w)
    v =np.sqrt(np.dot(w.T, np.dot( rt.cov() , w)))
    return v
def get_return(w):
    w = np.array(w)
    return np.sum(rt.mean()*w)
for R in rt_arr:
    cnt= ( {'type' : 'eq' , 'fun' : sum_one})#, {'type' : 'eq' , 'fun' : lambda w : get_return(w) - R} )
    opt = minimize( min_vol , w_0, method = 'SLSQP' , bounds = B , constraints = cnt)
    volatility_opt.append(opt)

for volt in volatility_opt:
    print([format(v,'.5f') for v in volt.x])
"""