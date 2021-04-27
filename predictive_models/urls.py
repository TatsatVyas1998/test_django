from django.urls import path
from predictive_models import views
from predictive_models.views import stock_view
urlpatterns = [
    path('', views.predictive_models_veiw , name = 'predictive_models'),
    path('load_stocks_list/' , stock_view.as_view() , name = 'jscript'),
    path('add_stock/' , views.add_stock, name = 'add_stock'),
    path('autosuggest/' , views.autosuggest, name = 'autosuggest'),
    path('create_portfolio/' , views.create_portfolio, name = 'create_portfolio'),
    path('portfolio_testing/' , views.portfolio_testing , name = 'portfolio_testing'),
    path('included_stocks/<task_id>', views.included_stocks, name='included_stocks'),
    path('portfolio_weights/<task_id>', views.portfolio_weights, name='portfolio_weights'),
    path('invest/', views.invest , name = 'invest')
]
