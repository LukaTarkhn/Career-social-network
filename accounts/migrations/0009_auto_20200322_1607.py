# Generated by Django 3.0.4 on 2020-03-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200322_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='last name'),
        ),
    ]
