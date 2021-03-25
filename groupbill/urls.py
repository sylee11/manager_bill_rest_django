from django.urls import path, re_path, include
from .views import GroupBillViewSet, BillViewSet, POViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'group', GroupBillViewSet)
router.register(r'bill', BillViewSet)
router.register(r'po', POViewSet)
urlpatterns = router.urls
