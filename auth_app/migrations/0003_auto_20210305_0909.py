# Generated by Django 3.0.8 on 2021-03-05 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_auto_20210304_1342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userapp',
            options={'permissions': [('can_change_status', 'Thay đổi trạng thái bộ hóa đơn'), ('can_export_excel', 'Xuất file excel')]},
        ),
    ]
