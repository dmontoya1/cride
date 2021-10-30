"""Circles model"""

#Django
from django.db import models

# Utilities
from cride.utils.models import CRideModel


class Circle(CRideModel):
    """Circle Model

    A circle is a private group where riders are offered and taken from
    by its members. to join a circle a uer must receive an unique
    invitation code from an existing circle member
    """

    name = models.CharField('circle name', max_length=255)
    slug_name = models.SlugField(max_length=40)

    about = models.CharField('Circle description', max_length=255)
    picture = models.ImageField(upload_to='circle/pictures/', blank=True, null=True)

    # Stats
    rides_offered = models.IntegerField(default=0)
    rides_taken = models.IntegerField(default=0)

    verified = models.BooleanField(
        'Verified circle',
        default=False,
        help_text='Verified circle are also know as official communities'
    )
    is_public = models.BooleanField(
        default=True,
        help_text='Public circles are listed in the main page so every know about their existence'
    )
    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circle can grown up to a fixed number of members'
    )
    members_limited = models.PositiveIntegerField(
        default=0,
        help_text='If circle is limited, this will be the limit on the number of members'
    )

    def __str__(self):
        """Return circle name"""
        return self.name

    class Meta(CRideModel.Meta):
        """Meta Class"""
        verbose_name = 'Circulo'
        ordering = ['-rides_taken', '-rides_offered']
