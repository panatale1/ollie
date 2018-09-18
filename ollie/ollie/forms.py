'''Forms for Ollie code screen'''

from django import forms

from .models import UserInfo


class InfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
