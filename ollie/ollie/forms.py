'''Forms for Ollie code screen'''

from datetime import datetime

import django_superform

from django import forms

from .models import OllieUser, PetInfo


class PetInfoForm(forms.ModelForm):
    dog_name = forms.CharField(label='Your pup\'s name')
    sterilized = forms.NullBooleanField(
        label='Your pup sterilized', widget=forms.CheckboxInput())
    primary_breed = forms.CharField(max_length=64, required=False)
    secondary_breed = forms.CharField(max_length=64, required=False)
    dry_food = forms.NullBooleanField(widget=forms.CheckboxInput())
    wet_food = forms.NullBooleanField(widget=forms.CheckboxInput())
    raw_food = forms.NullBooleanField(widget=forms.CheckboxInput())
    freeze_dried_food = forms.NullBooleanField(widget=forms.CheckboxInput())
    home_cooked_food = forms.NullBooleanField(widget=forms.CheckboxInput())
    fresh_food = forms.NullBooleanField(widget=forms.CheckboxInput())
    lineage = forms.ChoiceField(
        label='Your pup is a(n)',
        choices=(
            ('single breed', 'single breed'),
            ('mix of two breeds', 'mix of two breeds'),
            ('unknown mix', 'unknown mix')
        )
    )
    birth_year = forms.IntegerField(max_value=datetime.now().year, min_value=1991)

    class Meta:
        model = PetInfo
        fields = [
            'dog_name', 'lineage', 'primary_breed', 'secondary_breed', 'sex',
            'sterilized', 'birth_month', 'birth_year', 'activity_level',
            'weight', 'body_type', 'primary_protein', 'allergies', 'dry_food',
            'wet_food', 'raw_food', 'freeze_dried_food', 'home_cooked_food',
            'fresh_food'
        ]


class PetInfoField(django_superform.ModelFormField):

    def get_instance(self, form, name):
        try:
            if form.instance.pets.exists():
                return form.instance.pets.last()
            else:
                return None
        except PetInfo.DoesNotExist:
            return None

    def get_prefix(self, form, name):
        return name

    def save(self, form, name, composite_form, commit):
        pet = super(PetInfoField, self).save(
            form, name, composite_form, False)
        if pet:
            pet.owner = form.instance
            if commit:
                pet.save()
        return pet

class OllieSignUpForm(django_superform.SuperModelForm):
    username = forms.CharField(label='Your name')
    pet = PetInfoField(PetInfoForm)

    class Meta:
        model = OllieUser
        fields = ['username', 'zip_code', 'email']

    def clean(self):
        data = super(OllieSignUpForm, self).clean()
        return data
