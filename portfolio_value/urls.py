from django.urls import path
from portfolio_value import views

urlpatterns = [
    path('', views.portfolio , name = 'portfolio'),
    path('sell/<task_id>', views.sell_asst, name='sell_asst')
]
