# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.db.models import Sum
from celery.schedules import crontab
#from django.views.generic import View
#from .tasks import background_task
from . import models
from django.views import View
from django.core import serializers
import json
from .forms import PaymentForm
from .tasks import *
from some_name.models import *
import random


def home(request):
    # return HttpResponse("Hello!")
    form = PaymentForm()
    return render(request, "index.html", {'form': form})


class paymentView(View):
    def get(self, request):
        payments = Payment.objects.all()
        periodic_background_task.delay()
        # return render(request, "index.html", {'payments': payments})
        # background_task.delay()
        return JsonResponse(json.loads(serializers.serialize('json', payments)), safe=False)
        #return payments
    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            # details = {'username': request.POST['Username'], 'amount': request.POST['Amount']}
            user = User.objects.create(
                username=request.POST['Username']
            )
            Payment.objects.create(
                amount=request.POST['Amount'],
                payment_id = str(random.randint(1, 5)),
                user=user
            )
            return HttpResponse('Payment Successful, Status code 200')
            # return JsonResponse(details, safe=False)
        else:
            return HttpResponse('Payment Failed, Status code 400')


class userView(View):
    def get(self, request):
        #user = User.objects.all()
        #background_task.delay()
        user = Payment.objects.filter(user__pk="5")
        #user = Payment.objects.all()
        return JsonResponse(json.loads(serializers.serialize('json', user)), safe=False)

class userSum(View):
    def get(self, request):

        userSum = Payment.objects.filter(user__pk="5").aggregate(Sum('amount'))
        return HttpResponse(userSum.get('amount__sum'))

class userSuccess(View):
    """
    Get the Success Rate of the Seller
    Success Rate == No of Transactions (status == True) / No of Transactions(status == None) + No of Transactions (status == True)
    """
    def get(self,request):
        total_success = Payment.objects.filter(user__pk='5').filter(status='True').count()
        total_payments = Payment.objects.filter(user__pk="5").count()
        success_rate = total_success/total_payments
        print("Success Rate is "+str(success_rate))
        return HttpResponse("<h2>Success Rate is </h2>"+str(success_rate))


