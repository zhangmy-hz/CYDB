# Generated by Django 2.1.15 on 2020-02-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saomiao',
            name='TA006',
            field=models.CharField(default='N', max_length=5),
        ),
        migrations.AddField(
            model_name='yundan',
            name='YUN010',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='yundan',
            name='YUN09',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
