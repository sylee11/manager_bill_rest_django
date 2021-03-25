from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from common.models import Branch
# Create your models here.

class UserApp(AbstractUser):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    is_lock = models.BooleanField(default=False)

    phone = models.CharField('Số điện thoại', max_length=20, null=True, blank=True)

    class Meta:
        permissions = [
            ("can_change_status", "Thay đổi trạng thái bộ hóa đơn"),
            ("can_export_excel", "Xuất file excel"),
        ]

class GroupExtend(models.Model):
    group = models.OneToOneField(Group, unique=True, on_delete=models.CASCADE)
    name = models.CharField('Tên bộ phận', max_length=255, null=False,default='')
