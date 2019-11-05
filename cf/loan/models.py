from django.db import models


# Create your models here.


class ApplicationData(models.Model):
    RequestedLoanAmount = models.FloatField(default=0)
    StatedCreditHistory = models.BigIntegerField(default=0)
    LegalEntityType = models.CharField(max_length=50)
    FilterID = models.BigIntegerField(default=0)
    CFRequestId = models.BigIntegerField(default=0)
    RequestDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    CFApiUserId = models.CharField(max_length=50, null=True)
    CFApiPassword = models.CharField(max_length=50, null=True)
    IsTestLead = models.BooleanField(default=False)

    def __str__(self):
        return str(self.CFRequestId)


class Business(models.Model):
    ApplicationData = models.ForeignKey(ApplicationData, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=200)
    AnnualRevenue = models.FloatField(default=0)
    MonthlyAverageBankBalance = models.FloatField(default=0)
    MonthlyAverageCreditCardVolume = models.FloatField(default=0)
    Address1 = models.CharField(max_length=200)
    Address2 = models.CharField(max_length=200, null=True)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zip = models.CharField(max_length=5)
    TaxID = models.CharField(max_length=10)
    Phone = models.CharField(max_length=10)
    NAICS = models.CharField(max_length=6)
    HasBeenProfitable = models.BooleanField(default=False)
    HasBankruptedInLast7Years = models.BooleanField(default=False)
    InceptionDate = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.Name)


class Owner(models.Model):
    Business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=200)
    FirstName = models.CharField(max_length=26)
    LastName = models.CharField(max_length=26)
    Email = models.CharField(max_length=50)
    Address1 = models.CharField(max_length=200)
    Address2 = models.CharField(max_length=200, null=True)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zip = models.CharField(max_length=5)
    DateOfBirth = models.DateTimeField(auto_now=False, auto_now_add=False)
    HomePhone = models.CharField(max_length=10)
    SSN = models.CharField(max_length=9)
    PercentageOfOwnership = models.FloatField(default=0)

    def __str__(self):
        return str(self.Name)
