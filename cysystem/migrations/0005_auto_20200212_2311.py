# Generated by Django 2.1.15 on 2020-02-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysystem', '0004_yundan_yun015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yundan',
            name='YUN015',
            field=models.CharField(default='N', max_length=20),
        ),
    ]
