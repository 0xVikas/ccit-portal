# Generated by Django 2.2.4 on 2019-10-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190919_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='category',
            field=models.TextField(choices=[('FD', 'First Degree'), ('HD', 'Higer Degree'), ('PD', 'PhD')], null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='enrollment_year',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
