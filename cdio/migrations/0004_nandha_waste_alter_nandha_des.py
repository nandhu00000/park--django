# Generated by Django 4.2.7 on 2023-11-12 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdio', '0003_usful_delete_thanks_nandha_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='nandha',
            name='waste',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='nandha',
            name='des',
            field=models.CharField(null=True),
        ),
    ]
