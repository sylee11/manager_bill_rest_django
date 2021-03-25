from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Site, Permission, Branch, StatusBill, TypeProduct, Role, RolePermission
from .serializers import SiteSerializer, BranchSerializer, StatusBillSerializer, TypeProductSerializer, PermissionSerializer, RolePermissionSerializer, RoleSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
# Create your views here.

class SiteViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class PermissionViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class StatusBillViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = StatusBill.objects.all()
    serializer_class = StatusBillSerializer

class TypeProductViewSet(ModelViewSet):
    queryset = TypeProduct.objects.all()
    serializer_class = TypeProductSerializer

class BranchViewSet(ModelViewSet):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Branch.objects.all()
    serializer_class = BranchSerializer