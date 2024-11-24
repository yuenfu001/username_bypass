from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

# Create your models here.
class AccountManager(BaseUserManager):
    def _create_user(self, username,email, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError("The email is not provided")
        if not password:
            raise ValueError("Password not porvided")
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            **extra_fields
        )
    
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username,email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', False)
        return self._create_user(username, email, password, first_name, last_name, **extra_fields)

    def create_superuser(self, username,email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        return self._create_user(username, email, password, first_name, last_name, **extra_fields)



class Account(AbstractBaseUser,PermissionsMixin):
    # AbstractBaseUser has password, last login, is_active by default
    username = models.CharField(max_length=254, unique=True)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now_add=True)
    is_admin = models.BooleanField(default=False) # must needed, otherwise you can login to django-admin
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # must needed, otherwise you can login to django-admin
    is_superuser = models.BooleanField(default=False) # must needed, otherwise you can login to django-admin

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name', "last_name"]

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'