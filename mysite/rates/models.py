from django.db import models


class Bank(models.Model):
    bank_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    head_office_city = models.CharField(max_length=100)
    head_office_address = models.CharField(max_length=100)
    head_office_phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=255)
    usd_buy = models.DecimalField(max_digits=10, decimal_places=2)
    usd_sell = models.DecimalField(max_digits=10, decimal_places=2)
    eur_buy = models.DecimalField(max_digits=10, decimal_places=2)
    eur_sell = models.DecimalField(max_digits=10, decimal_places=2)
    rub_buy = models.DecimalField(max_digits=5, decimal_places=2)
    rub_sell = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.bank_name


class BankBranches(models.Model):
    branch_number = models.IntegerField(null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.address
