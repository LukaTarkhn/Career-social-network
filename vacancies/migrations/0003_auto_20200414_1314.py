# Generated by Django 3.0.4 on 2020-04-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_auto_20200414_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description'),
        ),
    ]
