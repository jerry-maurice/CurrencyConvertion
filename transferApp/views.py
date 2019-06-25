from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone
from datetime import datetime

# import models
from .models import Rate, Transaction

# dashboard
@login_required
def dashboard(request):
    #rateList = Rate.objects.all()
    #output = ', '.join([q.rateItems for q in rateList])
    dollar_unit = get_object_or_404(Rate, currency_from="US Dollar")
    peso_unit = get_object_or_404(Rate, currency_from="Peso")
    euro_unit = get_object_or_404(Rate, currency_from="Euro")
    canada_unit = get_object_or_404(Rate, currency_from="Canada Dollar")
    user_transfer = Transaction.objects.all().filter(transfer_by = request.user,
                                                     transfer_Date = timezone.now())
    context = {'dollar':dollar_unit, 'peso':peso_unit,
               'euro':euro_unit, 'canada':canada_unit,
               'transaction':user_transfer}
    return render(request,'transferApp/home.html', context)

# transfer
@login_required
def transfer(request):
    if request.method == 'GET':
        dollar_unit = get_object_or_404(Rate, currency_from="US Dollar")
        peso_unit = get_object_or_404(Rate, currency_from="Peso")
        euro_unit = get_object_or_404(Rate, currency_from="Euro")
        canada_unit = get_object_or_404(Rate, currency_from="Canada Dollar")
        context = {'dollar':dollar_unit, 'peso':peso_unit,
                   'euro':euro_unit, 'canada':canada_unit}
        return render(request, 'transferApp/transaction.html', context)
    elif request.method == 'POST':
        origin = request.POST["origingCurrency"]
        originAmount = request.POST["receiveAmount"]
        givenAmount = request.POST["giveAmount"]
        rate = request.POST["unitRate"]
        givenAmountVerification = float(rate) * float(originAmount)
        if givenAmountVerification != givenAmount:
            givenAmount = givenAmountVerification
        comment = request.POST["commentTransfer"]
        transfer_by = request.user
        transaction = Transaction(transfer_origin=origin,transfer_originAmount=originAmount,
                                  transfer_givenAmount=givenAmount, rate=rate,
                                  transfer_comment=comment, transfer_by = transfer_by)
        transaction.save()
        return redirect(dashboard)

# profile
@login_required
def profile(request):
    return render(request, 'transferApp/profile.html')



