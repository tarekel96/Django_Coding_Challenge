from django import forms
from .models import User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'nickname', 'profile_image']
