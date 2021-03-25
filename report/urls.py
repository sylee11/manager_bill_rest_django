from .views import RecordReportViewSet, ReportViewSet
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register(r'report', ReportViewSet)
route.register(r'record_report', RecordReportViewSet)
urlpatterns = route.urls