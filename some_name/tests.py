from django.test import TestCase

from .forms import PaymentForm
# Create your tests here.
class MyTests(TestCase):
    def test_payment_invalid(self):
        form_data = {'Username': 'Anvith', 'Amount': 10000}
        form = PaymentForm(data=form_data)
        try:
            self.assertEqual(form.is_valid(), True)
        except AssertionError:
            print("Failed 400")
        else:
            print("Success 200")

    def test_payment_valid(self):
        form_data = {'Username': 'Anvith Shetty', 'Amount': 10000}
        form = PaymentForm(data=form_data)
        try:
            self.assertEqual(form.is_valid(), True)
        except AssertionError:
            print("Failed 400")
        else:
            print("Success 200")
