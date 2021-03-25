from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(Site)
admin.site.register(RolePermission)
admin.site.register(Branch)
admin.site.register(StatusBill)
admin.site.register(TypeProduct)
admin.site.register(Company)