# Generated by Django 2.1.15 on 2020-02-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yundan',
            name='YUN011',
            field=models.CharField(default='Y', max_length=20),
        ),
        migrations.AlterField(
            model_name='yundan',
            name='YUN012',
            field=models.CharField(default='00-00-00', max_length=20),
        ),
        migrations.AlterField(
            model_name='yundan',
            name='YUN013',
            field=models.CharField(default='Y', max_length=20),
        ),
        migrations.AlterField(
            model_name='yundan',
            name='YUN014',
            field=models.CharField(default='00-00-00', max_length=20),
        ),
    ]
