from django.contrib.auth.models import User
import json
import os
from .views import *
from .models import *
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from rest_framework.response import Response
from django.urls import reverse


# Create your tests here.
class CreateLoanApplicationTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='admin',password='pass')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def testCreateLoanApplication(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, 'sample.json'), 'r') as jsonFile:
            request = json.load(jsonFile)
        url = reverse('loanapp')
        response = self.client.post(url, json.dumps(request), content_type='application/json')
        self.assertTrue(response.status_code == 200)

class TestLoanApplicationStatusTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='admin', password='pass')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def testLoanApplicationStatus(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, 'sample.json'), 'r') as jsonFile:
            request = json.load(jsonFile)
        url = reverse('loanapp')
        appResponse = self.client.post(url, json.dumps(request), content_type='application/json')
        self.assertTrue(appResponse.status_code == 200)
        loanAppId = appResponse.data['LoanAppID']
        url = reverse('status')
        statusResponse = self.client.get(url,data = {'LoanAppID': loanAppId})
        self.assertTrue('Processing' == 'Processing')
