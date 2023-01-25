from django.shortcuts import render
from django.http import HttpResponse
from .models import Bank, BankBranches


def index(request):
    bank = Bank.objects.all()

    context = {
        'bank': bank,
        'title': 'Rates.am',
    }

    return render(request, template_name="ratesPages/index.html", context=context)


def branches(request):
    branch = BankBranches.objects.all()
    context = {
        'branch': branch
    }
    return render(request, template_name="ratesPages/branches.html", context=context)
