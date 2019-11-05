from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer

from loan.models import *

class ApplicationDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationData
        fields = ('__all__')

class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = ('__all__')

class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = ('__all__')

