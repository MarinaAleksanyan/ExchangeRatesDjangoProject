from django.shortcuts import render
from django.http import HttpResponse
from .models import Bank, BankBranches


def index(request):
    bank = Bank.objects.all()
    branch = BankBranches.objects.all()

    context = {
        'bank': bank,
        'branch': branch,
        'title': 'Rates.am',
    }

    return render(request, template_name="ratesPages/index.html", context=context)


def branches(request, bank_id):
    branch = BankBranches.objects.filter(bank_id=bank_id)
    banks = Bank.objects.all()
    bank = Bank.objects.get(pk=bank_id)
    context = {
        'branch': branch,
        'bank': bank,
        'banks': banks,
        'title': 'Rates.am',
    }
    return render(request, template_name="ratesPages/branches.html", context=context)
