# Generated by Django 4.2.7 on 2023-12-06 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdio', '0008_alter_login_record_department_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login_record',
        ),
        migrations.DeleteModel(
            name='signup',
        ),
    ]
