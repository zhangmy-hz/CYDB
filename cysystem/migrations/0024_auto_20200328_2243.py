# Generated by Django 2.1.15 on 2020-03-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysystem', '0023_auto_20200328_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='yun_order',
            name='OR017',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='yun_order',
            name='OR015',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
