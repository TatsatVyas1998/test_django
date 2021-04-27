from django.urls import path
from top_movers import views

urlpatterns = [
    path('', views.top_movers , name = 'top')
]
