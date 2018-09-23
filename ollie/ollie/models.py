'''Models for the Ollie code screen'''

from django.db import models


class OllieUser(models.Model):
    username = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10)
    email = models.CharField(max_length=64)

    @property
    def pets(self):
        return self.pets.count()


class PetInfo(models.Model):
    LINEAGE_CHOICES = (
        ('single breed', 'single breed'),
        ('mix of two breeds', 'mix of two breeds'),
        ('unknown mix', 'unknown mix')
    )
    SEX_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )
    MONTHS = (
        ('Jan', 'Jan'),
        ('Feb', 'Feb'),
        ('Mar', 'Mar'),
        ('Apr', 'Apr'),
        ('May', 'May'),
        ('Jun', 'Jun'),
        ('Jul', 'Jul'),
        ('Aug', 'Aug'),
        ('Sep', 'Sep'),
        ('Oct', 'Oct'),
        ('Nov', 'Nov'),
        ('Dec', 'Dec')
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
    owner = models.ForeignKey(OllieUser, related_name='pets')
    dog_name = models.CharField(max_length=64)
    lineage = models.CharField(choices=LINEAGE_CHOICES, max_length=17)
    primary_breed = models.CharField(max_length=50)
    secondary_breed = models.CharField(max_length=50)
    sex = models.CharField(choices=SEX_CHOICES, max_length=6)
    sterilized = models.NullBooleanField()
    birth_month = models.CharField(choices=MONTHS, max_length=3)
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
