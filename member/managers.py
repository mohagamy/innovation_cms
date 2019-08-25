"""This creates a special user manager."""
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.base_user import BaseUserManager

from core.models import InnovationCMSManager


class UserManager(BaseUserManager, InnovationCMSManager):
    use_in_migrations = True

    def get_by_natural_key(self, key):
        try:
            return self.get(email=key)
        except ObjectDoesNotExist:
            return self.get(username=key)

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('There is no given email.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields['is_superuser'] = False
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_superuser'] = True
        return self._create_user(email, password, **extra_fields)
