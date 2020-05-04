# Generated by Django 3.0.4 on 2020-04-14 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0004_auto_20200409_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=30, unique=True, verbose_name='Url field')),
                ('title', models.CharField(max_length=150, null=True, verbose_name='Vacancy title')),
                ('qualification', models.CharField(choices=[('1', 'Intern'), ('2', 'Junior'), ('3', 'Middle'), ('4', 'Senior'), ('5', 'Lead')], max_length=10, null=True, verbose_name='Qualification')),
                ('salary', models.IntegerField(blank=True, max_length=15, null=True, verbose_name='Salary')),
                ('location', models.CharField(blank=True, max_length=80, null=True, verbose_name='Location')),
                ('work_type', models.CharField(choices=[('1', 'Full Time'), ('2', 'Part Time')], default='1', max_length=15, null=True, verbose_name='Work type')),
                ('remote_work', models.BooleanField(default=False, verbose_name='Remote work')),
                ('description', models.TextField(blank=True, max_length=250, null=True, verbose_name='Description')),
                ('bonuses', models.TextField(blank=True, max_length=250, null=True, verbose_name='Bonuses')),
                ('instructions', models.TextField(blank=True, max_length=250, null=True, verbose_name='Instructions')),
                ('sphere', models.CharField(blank=True, choices=[('1', 'backend'), ('2', 'frontend'), ('3', 'design'), ('4', 'administration'), ('5', 'analytics'), ('6', 'testing'), ('7', 'management'), ('8', 'marketing'), ('9', 'telekom'), ('10', 'sales'), ('11', 'applications'), ('12', 'software'), ('13', 'other')], max_length=20, null=True, verbose_name='Work type')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization')),
            ],
        ),
    ]