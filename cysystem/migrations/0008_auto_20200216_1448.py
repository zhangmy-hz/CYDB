# Generated by Django 2.1.15 on 2020-02-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysystem', '0007_yun_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yun_order',
            name='OR008',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='yun_order',
            name='OR009',
            field=models.IntegerField(default=0),
        ),
    ]