from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import  GroupBill, Bill, RecordBill, Po, RecordPo
from .serializers import GroupBillSerializer, BillSerializer, PoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.response import Response
# Create your views here.

class GroupBillViewSet(ModelViewSet):
    serializer_class = GroupBillSerializer
    queryset = GroupBill.objects.all()
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
class BillViewSet(ModelViewSet):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()
    def list(self, request, *args, **kwargs):
        return Response([])
class POViewSet(ModelViewSet):
    serializer_class = PoSerializer
    queryset = Po.objects.all()
