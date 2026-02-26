from dataclasses import fields

from .models import Profile
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ProfileAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))
        

class RegistrationFormStep1(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password_1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password_1') != cleaned_data.get('password_2'):
            self.add_error('password_2', "Passwords do not match.")
        if cleaned_data.get('email') and Profile.objects.filter(email=cleaned_data['email']).exists():
            self.add_error('email', "An account with this email already exists.")
        return cleaned_data

class RegistrationFormStep2(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    user_type = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=Profile.UserType.choices, initial=Profile.UserType.BARHOPPER)
    accept_terms = forms.BooleanField(required=True)
    
class ProfileUpdateForm(forms.ModelForm):
    fields = [
        'username',
        'email',
        'password',
        'first_name',
        'last_name',
        'date_of_birth',
        'user_type',
        'bio'
    ]
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'bio': forms.TextInput(attrs={'class': 'form-control'}),

        'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        'user_type': forms.Select(attrs={'class': 'form-control'}),
    }

    class Meta:
        model = Profile
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'date_of_birth',
            'bio',
            'password'
        ]
