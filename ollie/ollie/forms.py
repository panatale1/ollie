'''Forms for Ollie code screen'''

from datetime import datetime

import django_superform

from django import forms

from .models import OllieUser, PetInfo


class PetInfoForm(forms.ModelForm):
    dog_name = forms.CharField(label='Your pup\'s name is')
    sterilized = forms.NullBooleanField(
        label='Your pup is spayed or neutered', widget=forms.CheckboxInput())
    primary_breed = forms.CharField(max_length=64, required=False)
    secondary_breed = forms.CharField(max_length=64, required=False)
    dry_food = forms.BooleanField(
        widget=forms.CheckboxInput(),
        error_messages={'required': 'Please select at least one'})
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
    allergies = forms.CharField(
        widget=forms.Textarea({'cols': 20, 'rows': 1}),
        error_messages={
            'required': 'If your dog is not allergic to anything, please enter "nothing"'
        }
    )

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
    username = forms.CharField(label='Your name is')
    pet = PetInfoField(PetInfoForm)

    class Meta:
        model = OllieUser
        fields = ['username', 'zip_code', 'email']

    def clean(self):
        data = super(OllieSignUpForm, self).clean()
        if (self.data['pet-lineage'].lower() == 'single breed' and
                not self.data['pet-primary_breed']):
            self.forms['pet'].fields['primary_breed'].required = True
        elif (self.data['pet-lineage'].lower() == 'mix of two breeds' and
                not self.data['pet-primary_breed'] and not self.data['pet-secondary_breed']):
            self.forms['pet'].fields['primary_breed'].required = True
            self.forms['pet'].fields['secondary_breed'].required = True
        if ('pet-dry_food' not in self.data.keys() and
                'pet-wet_food' not in self.data.keys() and
                'pet-raw_fod' not in self.data.keys() and
                'pet-fresh_food' not in self.data.keys() and
                'pet-freeze_dried_food' not in  self.data.keys() and
                'pet-home_cooked_food' not in self.data.keys()):
            self.forms['pet'].fields['dry_food'].required = True
        return data
