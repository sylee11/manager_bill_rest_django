# Generated by Django 3.0.8 on 2021-03-04 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0002_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_src', models.CharField(max_length=200, verbose_name='Tên ảnh')),
                ('symbol', models.CharField(blank=True, max_length=10, null=True, verbose_name='Ký hiệu hóa đơn')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Số hóa đơn')),
                ('money_no_tax_0', models.IntegerField(blank=True, null=True, verbose_name='Tiền chưa thuế 0%')),
                ('money_no_tax_5', models.IntegerField(blank=True, null=True, verbose_name='Tiền chưa thuế 5%')),
                ('money_no_tax_10', models.IntegerField(blank=True, null=True, verbose_name='Tiền chưa thuế 10%')),
                ('money_no_tax_another', models.IntegerField(blank=True, null=True, verbose_name='Tiền chưa thuế khác')),
                ('money_no_tax_sum', models.IntegerField(blank=True, null=True, verbose_name='Tổng tiền chưa thuế')),
                ('money_tax_0', models.IntegerField(blank=True, null=True, verbose_name='Tiền  thuế 0%')),
                ('money_tax_5', models.IntegerField(blank=True, null=True, verbose_name='Tiền  thuế 5%')),
                ('money_tax_10', models.IntegerField(blank=True, null=True, verbose_name='Tiền  thuế 10%')),
                ('money_tax_another', models.IntegerField(blank=True, null=True, verbose_name='Tiền  thuế khác')),
                ('money_tax_sum', models.IntegerField(blank=True, null=True, verbose_name='Tổng tiền  thuế')),
                ('money_full_tax_0', models.IntegerField(blank=True, null=True, verbose_name='Tiền  thuế 0%')),
                ('money_full_tax_5', models.IntegerField(blank=True, null=True, verbose_name='Tiền  thuế 5%')),
                ('money_full_tax_10', models.IntegerField(blank=True, null=True, verbose_name='Tiền  thuế 10%')),
                ('money_full_tax_another', models.IntegerField(blank=True, null=True, verbose_name='Tiền  thuế khác')),
                ('money_full_tax_sum', models.IntegerField(blank=True, null=True, verbose_name='Tổng tiền  thuế')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày sửa cuối')),
            ],
        ),
        migrations.CreateModel(
            name='GroupBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mã vendor')),
                ('receiver_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mã receiver')),
                ('po_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mã Po')),
                ('batch_end', models.IntegerField(default=0)),
                ('is_qa', models.BooleanField(default=False, verbose_name='Trạng thái QA')),
                ('is_hddt', models.BooleanField(default=False, verbose_name='Là HDDT')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày sửa cuối')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Branch')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Company')),
                ('status_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.StatusBill')),
            ],
        ),
        migrations.CreateModel(
            name='Po',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày sửa cuối')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groupbill.GroupBill')),
            ],
        ),
        migrations.CreateModel(
            name='RecordPo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mã hàng hóa')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên hàng hóa')),
                ('unit', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đơn vị')),
                ('amount', models.CharField(blank=True, max_length=100, null=True, verbose_name='Số lượng')),
                ('vat', models.CharField(blank=True, max_length=100, null=True, verbose_name='Thuế VAT')),
                ('money', models.CharField(blank=True, max_length=100, null=True, verbose_name='Thanh tiền')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày sửa cuối')),
                ('po', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groupbill.Po')),
            ],
        ),
        migrations.CreateModel(
            name='RecordBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mã hàng hóa')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên hàng hóa')),
                ('unit', models.CharField(blank=True, max_length=100, null=True, verbose_name='Đơn vị')),
                ('amount', models.CharField(blank=True, max_length=100, null=True, verbose_name='Số lượng')),
                ('vat', models.CharField(blank=True, max_length=100, null=True, verbose_name='Thuế VAT')),
                ('money', models.CharField(blank=True, max_length=100, null=True, verbose_name='Thanh tiền')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày sửa cuối')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groupbill.Bill')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='group_bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groupbill.GroupBill'),
        ),
    ]