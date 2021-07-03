from django.db import models


class Bank(models.Model):
    class Meta:
        verbose_name = "Bank"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=150, null=True)


class Rates(models.Model):
    class Meta:
        verbose_name = "Rates"

    def __str__(self):
        return self.bank.name

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    usa_export_rate = models.CharField(max_length=150, null=True)
    usa_import_rate = models.CharField(max_length=150, null=True)
    eur_import_rate = models.CharField(max_length=150, null=True)
    eur_export_rate = models.CharField(max_length=150, null=True)
    date_created = models.DateField(auto_now_add=True, editable=False)
