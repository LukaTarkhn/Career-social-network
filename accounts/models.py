from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        if not first_name:
            raise ValueError("Users must have an first name")
        if not last_name:
            raise ValueError("Users must have an last name")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    email = models.EmailField(verbose_name='email address', max_length=60, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=30)
    last_name = models.CharField(verbose_name='last name', max_length=40)
    username = models.CharField(max_length=30, unique=True)
    phone = models.CharField(verbose_name='Phone', max_length=40, null=True, blank=True)
    profile_pic = models.ImageField(verbose_name='profile picture', null=True, blank=True)
    about_me = models.TextField(verbose_name='about me', max_length=250, null=True, blank=True)
    birth_day = models.DateField(verbose_name='birth_day', null=True, blank=True)
    living_city = models.CharField(verbose_name='living city', max_length=100, null=True, blank=True)
    gender = models.CharField(verbose_name='gender', max_length=1, choices=GENDER_CHOICES, default='M')
    website = models.CharField(verbose_name='website', max_length=100, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin