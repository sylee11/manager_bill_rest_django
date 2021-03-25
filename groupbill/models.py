from django.db import models
from common.models import Branch, Site, Role, Permission, TypeProduct, StatusBill, Company
from auth_app.models import UserApp
# Create your models here.
class GroupBill(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    status_bill = models.ForeignKey(StatusBill, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    vendor_number = models.CharField('Mã vendor', max_length=20, null=True, blank=True)
    receiver_number = models.CharField('Mã receiver', max_length=20, null=True, blank=True)
    po_number = models.CharField('Mã Po', max_length=20, null=True, blank=True)
    batch_end = models.IntegerField(default=0)

    is_qa = models.BooleanField('Trạng thái QA', default=False)
    is_hddt = models.BooleanField('Là HDDT', default=False)

    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày sửa cuối', auto_now=True)



class Bill(models.Model):
    group_bill = models.ForeignKey(GroupBill, on_delete=models.CASCADE)

    image_src = models.CharField('Tên ảnh', max_length=200, null=False, blank=False)
    symbol = models.CharField('Ký hiệu hóa đơn', max_length=10, null=True, blank=True)
    number = models.CharField('Số hóa đơn', max_length=20, null=True, blank=True)

    money_no_tax_0 = models.IntegerField('Tiền chưa thuế 0%' , null=True, blank=True)
    money_no_tax_5 = models.IntegerField('Tiền chưa thuế 5%' , null=True, blank=True)
    money_no_tax_10 = models.IntegerField('Tiền chưa thuế 10%' , null=True, blank=True)
    money_no_tax_another = models.IntegerField('Tiền chưa thuế khác' , null=True, blank=True)
    money_no_tax_sum = models.IntegerField('Tổng tiền chưa thuế' , null=True, blank=True)

    money_tax_0 = models.IntegerField('Tiền  thuế 0%', null=True, blank=True)
    money_tax_5 = models.IntegerField('Tiền  thuế 5%', null=True, blank=True)
    money_tax_10 = models.IntegerField('Tiền  thuế 10%', null=True, blank=True)
    money_tax_another = models.IntegerField('Tiền  thuế khác', null=True, blank=True)
    money_tax_sum = models.IntegerField('Tổng tiền  thuế', null=True, blank=True)

    money_full_tax_0 = models.IntegerField('Tiền  thuế 0%', null=True, blank=True)
    money_full_tax_5 = models.IntegerField('Tiền  thuế 5%', null=True, blank=True)
    money_full_tax_10 = models.IntegerField('Tiền  thuế 10%', null=True, blank=True)
    money_full_tax_another = models.IntegerField('Tiền  thuế khác', null=True, blank=True)
    money_full_tax_sum = models.IntegerField('Tổng tiền  thuế', null=True, blank=True)

    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày sửa cuối', auto_now=True)

class RecordBill(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    sku = models.CharField('Mã hàng hóa', max_length=20, null=True, blank=True)
    name = models.CharField('Tên hàng hóa', max_length=100, null=True, blank=True)
    unit = models.CharField('Đơn vị', max_length=100, null=True, blank=True)
    amount = models.CharField('Số lượng', max_length=100, null=True, blank=True)
    vat = models.CharField('Thuế VAT', max_length=100, null=True, blank=True)
    money = models.CharField('Thanh tiền', max_length=100, null=True, blank=True)

    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày sửa cuối', auto_now=True)

class Po(models.Model):
    group = models.ForeignKey(GroupBill, on_delete=models.CASCADE)

    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày sửa cuối', auto_now=True)

class RecordPo(models.Model):
    po = models.ForeignKey(Po, on_delete=models.CASCADE)
    sku = models.CharField('Mã hàng hóa', max_length=20, null=True, blank=True)
    name = models.CharField('Tên hàng hóa', max_length=100, null=True, blank=True)
    unit = models.CharField('Đơn vị', max_length=100, null=True, blank=True)
    amount = models.CharField('Số lượng', max_length=100, null=True, blank=True)
    vat = models.CharField('Thuế VAT', max_length=100, null=True, blank=True)
    money = models.CharField('Thanh tiền', max_length=100, null=True, blank=True)

    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày sửa cuối', auto_now=True)


