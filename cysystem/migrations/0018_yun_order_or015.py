# Generated by Django 2.1.15 on 2020-03-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysystem', '0017_yundan_yun021'),
    ]

    operations = [
        migrations.AddField(
            model_name='yun_order',
            name='OR015',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
