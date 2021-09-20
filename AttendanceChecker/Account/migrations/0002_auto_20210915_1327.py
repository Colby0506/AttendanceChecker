# Generated by Django 3.1 on 2021-09-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_student',
            field=models.BooleanField(null=True, verbose_name='is_student'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_teacher',
            field=models.BooleanField(null=True, verbose_name='is_teacher'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='date_joined'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='last_login'),
        ),
    ]
