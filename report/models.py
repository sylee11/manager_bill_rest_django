from django.db import models
from groupbill.models import GroupBill
from auth_app.models import UserApp
# Create your models here.

class Report(models.Model):
    group = models.ForeignKey(GroupBill, on_delete=models.CASCADE)
    user_create = models.ForeignKey(UserApp, on_delete=models.CASCADE)

    comment = models.CharField('Chú thích', max_length=255, null=True, blank=True )
    solution = models.CharField('Hướng xử lí', max_length=255, null=True, blank=True)
    status = models.IntegerField('Trạng thái biên bản', choices=[[1, 'N'], [2, 'P'], [3, 'E']])
    number_driver = models.CharField('Biển số xe', max_length=30, null=True, blank=True)
    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày cập nhật cuối', auto_now=True)

class RecordReport(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    bill_number = models.IntegerField('Số hóa đơn', null=True, blank=True)
    sku = models.CharField('Mã sản phẩm', max_length=50, null=True, blank=True)
    amount = models.CharField('Số lượng', max_length=23, null=True, blank=True)
    unit = models.CharField('Đoen giá', max_length=20, null=True, blank= True)

    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày cập nhật cuối', auto_now=True)
