from  django.urls import re_path, include
from rest_framework.viewsets import ViewSet, ModelViewSet
from .serializers import   SiteSerializer
from .models import Site
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import SiteViewSet, PermissionViewSet, StatusBillViewSet, TypeProductViewSet, BranchViewSet

urlpatterns = [
]

router_site= DefaultRouter()
router_site.register(r'site', SiteViewSet)
router_site.register(r'permission', PermissionViewSet)
router_site.register(r'statusbill', StatusBillViewSet)
router_site.register(r'typeproduct', TypeProductViewSet)
router_site.register(r'branch', BranchViewSet)
urlpatterns += router_site.urls