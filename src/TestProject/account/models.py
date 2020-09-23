from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a unique User Name')
        if not date_of_birth:
            raise ValueError('Date Of Birth is mandatory')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            date_of_birth=date_of_birth
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, date_of_birth, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            date_of_birth=date_of_birth,
            password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class AccountUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=225, unique=True)
    username = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(verbose_name="date of birth (YYYY-MM-DD)")
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
