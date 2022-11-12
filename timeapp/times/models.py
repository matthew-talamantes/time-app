from django.db import models
from django.urls import reverse

import uuid
from phonenumber_field.modelfields import PhoneNumberField

from useraccount.models import CustomUser

# Create your models here.

STATE_ABBREVIATIONS = [
        (None, ''), ('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'),
        ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'),
        ('FM', 'Federated States of Micronesia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'),
        ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'),
        ('LA', 'Louisiana'), ('ME', 'Maine'), ('MH', 'Marshall Islands'), ('MD', 'Maryland'), ('MA', 'Massachusetts'),
        ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'),
        ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'),
        ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'),
        ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PW', 'Palau'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'),
        ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'),
        ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'),
        ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'),
    ]

class Client(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, editable=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='', blank=False)
    company = models.CharField(max_length=50, default='', blank=True)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(blank=True)
    address1 = models.CharField(max_length=100, default= '', blank=True)
    address2 = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    state = models.CharField(max_length=2, choices=STATE_ABBREVIATIONS, blank=True)
    zipCode = models.CharField(max_length=5, verbose_name='Zip Code', default='', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'user': self.user.uuid, 'client': self.uuid})

    
