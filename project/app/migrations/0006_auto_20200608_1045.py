# Generated by Django 2.2.4 on 2020-06-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_detail_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
