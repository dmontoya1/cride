"""User model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """ User model
    Extend from Django's AbstractUser, change the username field
    to email and add some extra field
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists'
        }
    )
    phone_regex = RegexValidator(
        regex=r'\+?1?+\d{9,15}$',
        message='Phone number must be entered in the format +999999999. Up to 15 digitis allowed',
    )
    phone_number = models.CharField(
        'Phone number',
        validators=[phone_regex],
        max_length=17,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Help easily distinguish user and perform queries.'
            'Client are the main type of user'
        )
    )
    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to True if user have verified its email address'
    )

    def __str__(self):
        """Return username"""
        return self.username

    def get_short_name(self):
        """Return username"""
        return self.username

    class Meta:
        verbose_name = 'Usuario'
