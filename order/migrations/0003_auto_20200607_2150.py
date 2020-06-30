# Generated by Django 3.0.4 on 2020-06-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='add_info',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='mode',
            field=models.IntegerField(choices=[(0, 'Chưa đặt'), (1, 'Đã đặt'), (2, 'Đã chấp nhận'), (3, 'Đã nhận hàng')], default=0),
        ),
    ]