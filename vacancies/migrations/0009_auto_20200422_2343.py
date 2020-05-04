# Generated by Django 3.0.4 on 2020-04-22 19:43

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0008_vacancyskill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='sphere',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Backend'), ('2', 'Frontend'), ('3', 'Design'), ('4', 'Administration'), ('5', 'Analytics'), ('6', 'Testing'), ('7', 'Management'), ('8', 'Marketing'), ('9', 'Telekom'), ('10', 'Sales'), ('11', 'Applications'), ('12', 'Software'), ('13', 'Other')], max_length=150, null=True, verbose_name='Sphere'),
        ),
    ]
