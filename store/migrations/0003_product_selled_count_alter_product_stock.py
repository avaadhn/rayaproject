# Generated by Django 4.2.4 on 2023-09-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='selled_count',
            field=models.IntegerField(default=0, verbose_name='تعداد فروش'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='موجودی محصول'),
        ),
    ]
