# Generated by Django 2.1.15 on 2020-02-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cysystem', '0010_auto_20200216_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='yundan',
            name='YUN016',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
