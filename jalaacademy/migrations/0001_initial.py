# Generated by Django 4.2 on 2023-04-09 02:12

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_fame', models.CharField(max_length=255)),
                ('emp_lame', models.CharField(max_length=255)),
                ('emp_email', models.CharField(max_length=1000)),
                ('emp_phone', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(blank=True)),
                ('emp_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('emp_address', models.CharField(max_length=2000)),
                ('emp_skills', django_mysql.models.ListTextField(models.CharField(max_length=1000), size=10)),
                ('emp_city', models.CharField(max_length=200)),
                ('emp_country', models.CharField(max_length=200)),
            ],
        ),
    ]
