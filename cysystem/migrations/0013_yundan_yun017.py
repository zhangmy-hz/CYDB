# Generated by Django 2.1.15 on 2020-03-05 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysystem', '0012_auto_20200229_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='yundan',
            name='YUN017',
            field=models.CharField(default='N', max_length=4),
        ),
    ]