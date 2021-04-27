from django.contrib import admin
from predictive_models.models import load_stocks , selected_stocks , created_portfolio

# Register your models here.
admin.site.register(load_stocks)
admin.site.register(selected_stocks)
admin.site.register(created_portfolio)
