from django import forms
from .models import User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'nickname', 'profile_image']
    # name = forms.CharField(label='name', max_length=200)
    # nickname = forms.CharField(label='nickname', max_length=200)
    # profile_image = forms.CharField(label='profile_image', max_length=200)
