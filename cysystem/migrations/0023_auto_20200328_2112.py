# Generated by Django 2.1.15 on 2020-03-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysystem', '0022_auto_20200325_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='yun_order',
            name='OR016',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='yun_order',
            name='OR015',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
