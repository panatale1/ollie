'''Models for the Ollie code screen'''

from django.db import models


class UserInfo(models.Model):
    LINEAGE_CHOICES = (
        ('single breed', 'single breed'),
        ('two breeds', 'two breeds'),
        ('unknown mix', 'unknown mix')
    )
    SEX_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )
    MONTHS = (
        (1, 'Jan'),
        (2, 'Feb'),
        (3, 'Mar'),
        (4, 'Apr'),
        (5, 'May'),
        (6, 'Jun'),
        (7, 'Jul'),
        (8, 'Aug'),
        (9, 'Sep'),
        (10, 'Oct'),
        (11, 'Nov'),
        (12, 'Dec')
    )
    ACTIVITY_CHOICES = (
        ('lazy', 'lazy'),
        ('active', 'active'),
        ('hyper', 'hyper')
    )
    BODY_CHOICES = (
        ('skinny', 'skinny'),
        ('ideal', 'ideal'),
        ('chubby', 'chubby')
    )
    owner_name = models.CharField(max_length=64)
    dog_name = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10)
    email = models.CharField(max_length=64)
    lineage = models.CharField(choices=LINEAGE_CHOICES, max_length=12)
    primary_breed = models.CharField(max_length=50)
    secondary_breed = models.CharField(max_length=50)
    sex = models.CharField(choices=SEX_CHOICES, max_length=6)
    sterilized = models.NullBooleanField()
    birth_month = models.CharField(choices=MONTHS, max_length=2)
    birth_year = models.IntegerField()
    activity_level = models.CharField(choices=ACTIVITY_CHOICES, max_length=6)
    weight = models.IntegerField()
    body_type = models.CharField(choices=BODY_CHOICES, max_length=6)
    primary_protein = models.CharField(max_length=20)
    allergies = models.TextField()
    dry_food = models.NullBooleanField()
    wet_food = models.NullBooleanField()
    raw_food = models.NullBooleanField()
    freeze_dried_food = models.NullBooleanField()
    home_cooked_food = models.NullBooleanField()
    fresh_food = models.NullBooleanField()



