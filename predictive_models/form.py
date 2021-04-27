from predictive_models.models import load_stocks
from django import forms

class add_stock( forms.ModelForm):
    class Meta:
        model = load_stocks
        fields = '__all__'

    def __init__(self , *args , **kwargs):
        super( ).__init__(*args, **kwargs)
        self.fields['stock_name'].queryset = load_stocks.objects.none()
