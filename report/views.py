from django.shortcuts import render
from .models import Report, RecordReport
from .serializers import RecordReportSerializer, ReportSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
# Create your views here.

class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

class RecordReportViewSet(ModelViewSet):
    queryset = RecordReport.objects.all()
    serializer_class = RecordReportSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]
