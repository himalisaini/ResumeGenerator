# Generated by Django 2.2.4 on 2020-06-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('email_id', models.CharField(max_length=300)),
                ('summary', models.TextField(max_length=2000)),
                ('degree', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=500)),
                ('university', models.CharField(max_length=500)),
                ('internship', models.TextField(max_length=2000)),
                ('work_experience', models.TextField(max_length=2000)),
                ('skills', models.TextField(max_length=1000)),
            ],
        ),
    ]
