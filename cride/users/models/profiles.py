""" Profiles model"""

# Django
from django.db import models

#Utilities
from cride.utils.models import CRideModel


class Profile(CRideModel):
    """ Profile Model
    A profile holds a user's public data like biography, picture
    and statistics.
    """

    user = models.OneToOneField(
        'users.User',
        verbose_name="Usuario",
        on_delete=models.CASCADE,
    )
    picture = models.ImageField(
        'Profile Picture',
        upload_to='user/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(
        'About me',
        max_length=500,
        blank=True
    )
    # Stats
    rides_taken = models.PositiveIntegerField(
        'Rides taken',
        default=0,
    )
    rides_offered = models.PositiveIntegerField(
        'Rides offered',
        default=0
    )
    reputations = models.FloatField(
        default=5.0,
        help_text='Users reputations based on the rides taken and offered'
    )

    def __str__(self):
        """ Return user's String representation"""
        return str(self.user)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
