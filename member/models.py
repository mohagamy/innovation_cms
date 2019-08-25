import imghdr
import datetime

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import InnovationCMSModel
from core.utlis import generate_file
from member.managers import UserManager


def generate_img_file(self, filename):
    return generate_file('profile_pics', filename)


def generate_resume_file(self, filename):
    return generate_file('resumes', filename)


def validate_avatar(value):
    """Check if avatar is a valid image or not."""
    avatar_type = imghdr.what(value)
    if avatar_type is None:
        raise ValidationError([{"avatar": u'%s is invalid image.' % value}])


class Member(AbstractBaseUser, PermissionsMixin, InnovationCMSModel):
    """Assessment User Model."""

    email = models.EmailField(
        _('Email Address'), unique=True,
        error_messages={
            'unique': "This Email has already been registered.",
            "blank": "Email can not be empty.",
            "null": "Email is a required field."})

    full_name = models.CharField(
        _('Full Name'), max_length=30, null=True, blank=True,
        error_messages={
            "max_length": "Full Name must be less than 30 characters."})

    username = models.CharField(
        max_length=30, unique=True,
        error_messages={
            'unique': "This Username has already been registered.",
            "max_length": "Username must be less than 30 characters.",
            "blank": "Username can not be empty.",
            "null": "Username is a required field."})

    profile_pic = models.ImageField(
        _('Profile Picture'), upload_to=generate_img_file,
        null=True, blank=True, validators=[validate_avatar])

    bio = models.TextField(null=True, blank=True)

    start_datetime = models.DateTimeField(default=datetime.datetime.now)

    end_datetime = models.DateTimeField(default=datetime.datetime.now)

    resume = models.FileField(
        _('Resume'), upload_to=generate_resume_file, null=True, blank=True)

    is_active = models.BooleanField(_('Active'), default=True)

    is_staff = models.BooleanField(_('Staff'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('Member')
        verbose_name_plural = _('Members')

    def get_short_name(self):
        """Return the short name for the user."""
        return self.full_name

    def __str__(self):
        return self.username
