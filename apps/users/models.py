from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from apps.users.constants import UserType
from apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.IntegerField(_('username'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    user_type = models.IntegerField(choices=UserType.get_choices())
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def get_avatar(self):
        """
        returns the url of the user avatar
        :return:
        """
        try:
            return self.avatar.url
        except ValueError:
            return None

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name