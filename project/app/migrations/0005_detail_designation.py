# Generated by Django 2.2.4 on 2020-06-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200608_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='designation',
            field=models.CharField(default='Student', max_length=100),
        ),
    ]
