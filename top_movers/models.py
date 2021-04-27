from django.db import models

# Create your models here.

class get_topmovers(models.Model):

    stock = models.CharField(max_length=100)
    move_val = models.FloatField(null= True , blank = True , default = None)
    prc_change = models.FloatField(null= True , blank = True , default = None)
    vol = models.CharField(max_length=100)
    def __str__(self):
        return self.stock
