from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField('Tên Mô hình', max_length=255, null=False, unique=True, blank=False)
    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày cập nhật cuối', auto_now=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField('Tên Chi Nhánh', max_length=500, null=False, unique=True, blank=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    address = models.TextField('Địa chỉ', null=True, blank=True)
    company_name = models.TextField('Tên Công Ty', null=True, blank=True)
    tax_number = models.CharField('Mã Số Thuế', max_length=13, null=False, blank=False,unique=True)
    store_number = models.BigIntegerField('Mã cửa hàng', null=False, blank=False, unique=True)
    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày cập nhật cuối', auto_now=True)
    is_ttpp = models.BooleanField('Là Trung Tâm Phân Phối', default=False)
    description = models.TextField('Mô tả', null=True,blank=True)
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField('Tên Bộ Phận', max_length=255, null=False, blank=False)
    symbol = models.CharField('Ký Hiệu', max_length=20, null=False, blank=False, unique=True )
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày cập nhật cuối', auto_now=True)

    def __str__(self):
        return self.name



class Permission(models.Model):
    name = models.CharField('Quyền',
        max_length=255,
        null=False,
        blank=False
    )
    symbol = models.CharField('Ký hiệu', null=False, blank=False, unique=True, max_length=100)
    role = models.ManyToManyField(Role, through='RolePermission', related_name="role_permission")
    type = models.IntegerField('Loại', null=False, blank=False, choices=[[1,'Hóa đơn'], [2, 'Bảng kê'], [3, 'Biên bản'], [4, 'Khác']], default=1)
    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày cập nhật cuối', auto_now=True)

    def __str__(self):
        return self.name

class RolePermission(models.Model):
    role = models.ForeignKey(Role, null=False, blank=False, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày cập nhật cuối', auto_now=True)


class StatusBill(models.Model):
    name = models.CharField(
        'Tên trạng thái',
        max_length=500,
        null=False,
        blank=False
    )
    symbol = models.CharField(
        'Ký hiệu',
        unique=True,
        max_length=10
    )
    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày cập nhật cuối', auto_now=True)

    def __str__(self):
        return self.name

class TypeProduct(models.Model):
    name = models.CharField(
        'Tên ngành hàng',
        max_length=500,
    )
    symbol = models.CharField(
        'Ký hiệu',
        unique=True,
        max_length=10
    )
    type = models.IntegerField(
        'Thuộc loại',
        null=False,
        default=1,
        choices=[
            [1,'Hàng khô'],
            [2,'Hàng ướt'],
            [3,'Bảng kê'],
        ]
    )
    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày cập nhật cuối', auto_now=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField('Tên công ty', max_length= 300, null=False, default='')
    address = models.CharField('Địa chỉ', max_length=300, null=False, default='')
    tax_number = models.CharField('Mã số thuế', max_length= 20, null=False, default='')
    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Ngày cập nhật cuối', auto_now=True)