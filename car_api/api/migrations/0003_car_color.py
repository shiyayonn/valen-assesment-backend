# Generated by Django 3.1.1 on 2020-09-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200916_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='red', max_length=10),
        ),
    ]
