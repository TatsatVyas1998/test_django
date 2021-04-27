from django.db import models
import json
# Create your models here.

class load_stocks(models.Model):
    stock_name = models.CharField(max_length=100)
    stock_symbol = models.CharField(max_length=100)
    def __str__(self):
        return self.stock_name


class selected_stocks(models.Model):
    stock_name = models.CharField(max_length=100)
    stock_symbol = models.CharField(max_length=100)
    def __str__(self):
        return self.stock_name

class created_portfolio(models.Model):
    stock_symbol = models.CharField(max_length = 200)
    port_weight_opt = models.CharField(max_length = 200)

    def add_symbol(self ,x):
        self.stock_symbol = json.dumps(x)
    def add_opt_weights(self , x):
        self.port_weight_opt = json.dumps(x)
    def get_symbol_list(self):
        return json.loads( self.stock_symbol)
    def get_opt_weights(self):
        return json.loads(self.port_weight_opt)
