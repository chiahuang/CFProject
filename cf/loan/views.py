from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *
from drf_multiple_model.views import ObjectMultipleModelAPIView


class CreateLoanAppView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        requestHeader = request.data['RequestHeader']
        appData = request.data['CFApplicationData']
        newApplicationData = {**requestHeader, **appData}

        loanApplicationObj, loanApplicationCreated = ApplicationData.objects.update_or_create(
            CFRequestId=newApplicationData.pop('CFRequestId'),
            defaults=newApplicationData)
        loanApplicationObj.save()

        businessAddress = request.data['Business'].pop('Address')
        businessCashFlow = request.data['Business'].pop('SelfReportedCashFlow')
        businessData = {**request.data['Business'], **businessAddress, **businessCashFlow}
        businessObj, businessCreated = Business.objects.update_or_create(Name=request.data['Business'].pop('Name'),
                                                                         TaxID=request.data['Business'].pop('TaxID'),
                                                                         defaults=businessData)
        businessObj.ApplicationData = loanApplicationObj
        businessObj.save()

        for owner in request.data['Owners']:
            ownerAddress = owner.pop('HomeAddress')
            ownerData = {**owner, **ownerAddress}
            ownerObj, ownerCreated = Owner.objects.update_or_create(Name=owner.pop('Name'),
                                                                    SSN=owner.pop('SSN'),
                                                                    DateOfBirth=owner.pop('DateOfBirth'),
                                                                    defaults=ownerData)
            ownerObj.Business = businessObj
            ownerObj.save()

        return Response(status=200, data={'LoanAppID': str(loanApplicationObj.id)})


class GetLoanAppStatusView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        id = request.GET.get('id', None)
        if id:
            try:
                loanAppId = ApplicationData.objects.get(id=self.request.GET['id'])
                print('let me seee ', loanAppId)
                return Response(status=200, data={'Status': 'Processing.'})
            except:
                return Response(status=404, data={'Status': 'Id does not exist.'})
        else:
            return Response(status=400, data={'Status': 'Missing Id.'})