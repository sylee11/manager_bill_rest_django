from .models import *
from rest_framework import serializers

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class RecordReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordReport
        fields = '__all__'
        
