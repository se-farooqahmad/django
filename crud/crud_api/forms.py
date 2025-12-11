# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Username'].label = 'Email'



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username or Email')
