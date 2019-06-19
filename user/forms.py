from django.forms import ModelForm
from .models import UserProfile, Validation
from .models import CATEGORY, ENGINEERING, Settings
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import pdb


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        #pdb.set_trace()
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class RegistrationUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('registration_number', 'category', 'engineering')

    def save(self, commit=True):
        if self.is_valid():
            if self.instance.id == None:
                #pdb.set_trace()
                user_django = User.objects.last()
                user_profile = UserProfile.objects.create(
                    registration_number=self.cleaned_data['registration_number'],
                    category=self.cleaned_data['category'],
                    engineering=self.cleaned_data['engineering'],
                    user=user_django
                )
                return user_profile
