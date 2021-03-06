# Generated by Django 2.2.7 on 2019-11-05 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RequestedLoanAmount', models.FloatField(default=0)),
                ('StatedCreditHistory', models.BigIntegerField(default=0)),
                ('LegalEntityType', models.CharField(max_length=50)),
                ('FilterId', models.BigIntegerField(default=0)),
                ('CfRequestId', models.BigIntegerField(default=0)),
                ('RequestDate', models.DateTimeField()),
                ('CfApiUserId', models.CharField(max_length=50, null=True)),
                ('CfApiPassword', models.CharField(max_length=50, null=True)),
                ('IsTestLead', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('AnnualRevenue', models.FloatField(default=0)),
                ('MonthlyAverageBankBalance', models.FloatField(default=0)),
                ('MonthlyAverageCreditCardVolume', models.FloatField(default=0)),
                ('Address1', models.CharField(max_length=200)),
                ('Address2', models.CharField(max_length=200, null=True)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Zip', models.CharField(max_length=5)),
                ('TaxId', models.CharField(max_length=10)),
                ('Phone', models.CharField(max_length=10)),
                ('NAICS', models.CharField(max_length=6)),
                ('HasBeenProfitable', models.BooleanField(default=False)),
                ('HasBankruptedInLast7Years', models.BooleanField(default=False)),
                ('InceptionDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('FirstName', models.CharField(max_length=26)),
                ('LastName', models.CharField(max_length=26)),
                ('Email', models.CharField(max_length=50)),
                ('Address1', models.CharField(max_length=200)),
                ('Address2', models.CharField(max_length=200, null=True)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Zip', models.CharField(max_length=5)),
                ('DateOfBirth', models.DateTimeField()),
                ('HomePhone', models.CharField(max_length=10)),
                ('SSN', models.CharField(max_length=9)),
                ('PercentageOfOwnership', models.FloatField(default=0)),
            ],
        ),
    ]
