import pandas as pd
import numpy as np
from django.db import models
from models import load_stocks

df = pd.read_csv("./docs/stock_list.csv")
for i, row in df.iterrows():
    obj = load_stocks.objects.create(stock_name = row['Name'] , stock_symbol= row['Symbol'] )
    obj.save()
