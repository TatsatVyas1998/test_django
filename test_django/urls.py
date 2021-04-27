
from django.contrib import admin
from django.urls import path , include
from test_django import views
from predictive_models.views import stock_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('top/' , include('top_movers.urls') ),
    path('', views.home_page , name = 'home'),
    path('predictive_models/' , include('predictive_models.urls')),
    path('portfolio_testing/' , include('predictive_models.urls')),
    path('portfolio_value/' , include('portfolio_value.urls')),
    #path('load_stocks_list/' , stock_view.as_view()),
]
