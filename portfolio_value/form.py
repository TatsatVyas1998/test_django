from django import forms
from portfolio_value.models import portfolio_value


class add_stock( forms.ModelForm):
    class Meta:
        model = portfolio_value
        fields = ['stock' , 'your_equity', 'shares' , 'total_return' ]
