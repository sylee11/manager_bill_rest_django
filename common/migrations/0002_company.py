# Generated by Django 3.0.8 on 2021-03-04 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300, verbose_name='Tên công ty')),
                ('address', models.CharField(default='', max_length=300, verbose_name='Địa chỉ')),
                ('tax_number', models.CharField(default='', max_length=20, verbose_name='Mã số thuế')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật cuối')),
            ],
        ),
    ]