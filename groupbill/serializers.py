from rest_framework import serializers
from .models import *

class GroupBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupBill
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class PoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Po
        fields = '__all__'