from django import forms
from django.utils.safestring import mark_safe

class PaymentForm(forms.Form):
    Username = forms.CharField(max_length=40, min_length=10, label=mark_safe('<br/>Username'))
    Amount = forms.DecimalField(max_digits=12, decimal_places=2, label=mark_safe('<br/><br/>Amount'))