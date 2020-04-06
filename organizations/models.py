from django.db import models
from django.conf import settings


class Organization(models.Model):
    NUMBER_OF_EMPLOYEES = (
        ('1', '1'),
        ('10', '1-10'),
        ('100', '10-100'),
        ('1000', '100-1000'),
        ('5000', '1000+'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    url = models.CharField(verbose_name='Url field', max_length=30, unique=True)
    organization_name = models.CharField(verbose_name='Organization name', max_length=30, null=True)
    organization_phone = models.CharField(verbose_name='Organization phone', max_length=50, null=True, blank=True)
    organization_email = models.EmailField(verbose_name='Organization email', max_length=50, null=True, blank=True)
    organization_alter_names = models.CharField(verbose_name='Organization alternative names', max_length=50, null=True,
                                                blank=True)
    organization_logo = models.ImageField(verbose_name='Logo', null=True, blank=True)
    organization_header_logo = models.ImageField(verbose_name='Header logo', null=True, blank=True)
    organization_about = models.TextField(verbose_name='About organization', max_length=250, null=True, blank=True)
    organization_specialization = models.CharField(verbose_name='Organization specialization', max_length=70, null=True,
                                                   blank=True)
    organization_website = models.CharField(verbose_name='website', max_length=100, null=True, blank=True)
    organization_address = models.CharField(verbose_name='Organization address', max_length=100, null=True, blank=True)
    number_of_employees = models.CharField(verbose_name='Number of employees', max_length=100, null=True, blank=True,
                                           choices=NUMBER_OF_EMPLOYEES)
    date_created = models.DateTimeField(verbose_name='Create date', auto_now_add=True)

    def __str__(self):
        return str(self.user)
