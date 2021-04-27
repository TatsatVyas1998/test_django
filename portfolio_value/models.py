from django.db import models

# Create your models here.


class portfolio_value(models.Model):

    stock = models.CharField(max_length=100)
    shares = models.FloatField(null= True , blank = True , default = None)
    your_equity  = models.FloatField(null= True , blank = True , default = None)
    total_return = models.FloatField(null= True , blank = True , default = 0)
    def __str__(self):
        return self.stock
