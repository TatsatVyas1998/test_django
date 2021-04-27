from django.contrib import admin
from top_movers.models import get_topmovers
from portfolio_value.models import portfolio_value
# Register your models here.
admin.site.register(get_topmovers)
admin.site.register(portfolio_value)
