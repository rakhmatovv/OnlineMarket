from django import forms
from .models import Order
from .bulma_mixin import BulmaMixin


class OrderForm(BulmaMixin, forms.Form):
    address = forms.CharField(label='Write your address')
    phone = forms.CharField(label='Write your phone')

    class Meta:
        model = Order
        fields = ['address', 'phone']
