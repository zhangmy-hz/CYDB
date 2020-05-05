# Generated by Django 2.1.15 on 2020-02-11 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PURMA',
            fields=[
                ('MA001', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('MA002', models.CharField(max_length=30)),
                ('MA003', models.CharField(max_length=50)),
                ('MA004', models.CharField(max_length=30)),
                ('MA005', models.CharField(max_length=300)),
                ('MA006', models.CharField(max_length=10)),
                ('MA007', models.CharField(max_length=20)),
                ('MA008', models.CharField(max_length=10)),
                ('MA009', models.CharField(max_length=32, null=True)),
                ('MA010', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PURTC',
            fields=[
                ('TC001', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('TC002', models.CharField(max_length=20, null=True)),
                ('TC003', models.CharField(max_length=10, null=True)),
                ('TC004', models.CharField(max_length=10, null=True)),
                ('TC005', models.CharField(max_length=10, null=True)),
                ('TC006', models.CharField(max_length=255, null=True)),
                ('TC007', models.CharField(max_length=10, null=True)),
                ('TC008', models.CharField(max_length=60, null=True)),
                ('TC009', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='saomiao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TA001', models.CharField(max_length=20)),
                ('TA002', models.CharField(max_length=255)),
                ('TA003', models.CharField(max_length=50)),
                ('TA004', models.IntegerField(default=0)),
                ('TA005', models.CharField(default='N', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='User_CY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='yundan',
            fields=[
                ('YUN01', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('YUN02', models.CharField(max_length=20)),
                ('YUN03', models.CharField(max_length=20)),
                ('YUN04', models.CharField(max_length=20)),
                ('YUN05', models.CharField(max_length=20)),
                ('YUN06', models.CharField(max_length=20)),
                ('YUN07', models.CharField(max_length=20)),
                ('YUN08', models.CharField(max_length=20)),
                ('YUN09', models.CharField(max_length=20)),
            ],
        ),
    ]
