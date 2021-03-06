# Generated by Django 3.0.8 on 2021-02-01 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Quyền')),
                ('symbol', models.CharField(max_length=100, unique=True, verbose_name='Ký hiệu')),
                ('type', models.IntegerField(choices=[[1, 'Hóa đơn'], [2, 'Bảng kê'], [3, 'Biên bản'], [4, 'Khác']], default=1, verbose_name='Loại')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật cuối')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Tên Bộ Phận')),
                ('symbol', models.CharField(max_length=20, unique=True, verbose_name='Ký Hiệu')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật cuối')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Tên Mô hình')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật cuối')),
            ],
        ),
        migrations.CreateModel(
            name='StatusBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Tên trạng thái')),
                ('symbol', models.CharField(max_length=10, unique=True, verbose_name='Ký hiệu')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật cuối')),
            ],
        ),
        migrations.CreateModel(
            name='TypeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Tên ngành hàng')),
                ('symbol', models.CharField(max_length=10, unique=True, verbose_name='Ký hiệu')),
                ('type', models.IntegerField(choices=[[1, 'Hàng khô'], [2, 'Hàng ướt'], [3, 'Bảng kê']], default=1, verbose_name='Thuộc loại')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật cuối')),
            ],
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật cuối')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Role')),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Site'),
        ),
        migrations.AddField(
            model_name='permission',
            name='role',
            field=models.ManyToManyField(related_name='role_permission', through='common.RolePermission', to='common.Role'),
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True, verbose_name='Tên Chi Nhánh')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Địa chỉ')),
                ('company_name', models.TextField(blank=True, null=True, verbose_name='Tên Công Ty')),
                ('tax_number', models.CharField(max_length=13, unique=True, verbose_name='Mã Số Thuế')),
                ('store_number', models.BigIntegerField(unique=True, verbose_name='Mã cửa hàng')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật cuối')),
                ('is_ttpp', models.BooleanField(default=False, verbose_name='Là Trung Tâm Phân Phối')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Site')),
            ],
        ),
    ]
