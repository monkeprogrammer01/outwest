import jwt
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime, timedelta
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if email == None:
            raise TypeError("Users must have an email address.")

        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=256, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({"id": self.pk, "exp": int(dt.strftime('%s'))}, settings.SECRET_KEY, algorithm='HS256')

        return token
